import pygame
from pygame.locals import *
import sys
import numpy as np
import math
from objects.components.updater import updater
from objects.operations import modify_color

class drawingboard(updater):
    def __init__(self, screen,position, size=400,color=(0,0,255),axis_density=100,border_width=1,depth=1):
        self.screen = screen
        self.positionX=position[0]
        self.positionY=position[1]
        self.size=size
        self.axis_density=axis_density
        self.pixel_array =np.zeros((self.axis_density, self.axis_density), dtype='uint8')
        self.pixel_size = size//axis_density
        self.is_dragging = False
        self.start_pos = None
        self.line_width = 1
        self.line_color = color
        self.border_width = border_width
        self.depth=depth
        self.state="pen" #another state is "eraser" "fill" "line"
        self.showgrid=False
        
        self.grid_color=(255,33,81)
    
        super().__init__()
        
    def set_array(self,arr):
        self.pixel_array=arr
        
    def get_array(self):
        return self.pixel_array    
    
    def set_width(self,width):
        self.line_width=width

    def set_state(self,state):
        self.state=state
        
    def set_depth(self,depth):
        self.depth=depth
        
    def set_grid(self,showgrid):
        self.showgrid=showgrid
        
    def maintain(self,a):
        if(a<0):return 0;
        elif(a>=self.axis_density):return self.axis_density-1
        else:return a
        
    
    def screen_to_array(self, pos):
        if((pos[0]>self.positionX and pos[0]<self.positionX+self.size) and (pos[1]>self.positionY and pos[1]<self.positionY+self.size)):
            return (pos[0]-self.positionX) // self.pixel_size,( pos[1]-self.positionY) // self.pixel_size
        else:return None
        
    def array_to_screen(self,pos):
        return( (pos[0]*self.pixel_size)+self.positionX,(pos[1]*self.pixel_size)+self.positionY)
    
    def bresenham_line_algo(self, start_pos, end_pos):
        if(start_pos==None):return
        x0, y0 = start_pos
        x1, y1 = end_pos
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        err = dx - dy
        while True:
            # set the pixel to True
            
            self.pixel_array[self.maintain(y0),self.maintain(x0)] =self.depth
            
            # check if we've reached the end of the line
            if x0 == x1 and y0 == y1:
                break
            # calculate the next pixel to draw
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
                
    

    def angle_between_points(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        angle = math.atan2(y2-y1, x2-x1)
        angle=-1* math.degrees(angle)
        if(angle < 0):return 360+angle
        else:return angle
    

    def draw_line(self, start_pos, end_pos):
        self.bresenham_line_algo(start_pos, end_pos)
        angle=self.angle_between_points(start_pos,end_pos)
        if((135<angle<225) or (45>angle) or (angle>270)):
            for i in range(self.line_width):
                modified_start_pos = (start_pos[0],start_pos[1]-i)
                modified_end_pos=(end_pos[0],end_pos[1]-i)
                self.bresenham_line_algo(modified_start_pos, modified_end_pos)   
        else:
            for i in range(self.line_width):
                modified_start_pos = (start_pos[0]-i,start_pos[1])
                modified_end_pos=(end_pos[0]-i,end_pos[1])
                self.bresenham_line_algo(modified_start_pos, modified_end_pos)


    def flood_fill(self,position,value):
        if(position[0]<0 or position[0]>=self.axis_density or position[1]<0 or position[1]>=self.axis_density):return
        if(value==(self.depth)):return
        y,x=position
        stack = [(x, y)]
        # Iterate until the stack is empty
        while stack:
            # Pop the next pixel to fill from the stack
            x, y = stack.pop()
            # Check if the pixel needs to be filled
            if self.pixel_array[x][y] == value:
                # Fill the pixel with the new value
                self.pixel_array[x][y] = self.depth
                # Add adjacent pixels to the stack
                if x > 0:
                    stack.append((x - 1, y))  # Pixel to the left
                if x < self.axis_density - 1:
                    stack.append((x + 1, y))  # Pixel to the right
                if y > 0:
                    stack.append((x, y - 1))  # Pixel above
                if y <self.axis_density - 1:
                    stack.append((x, y + 1))  # Pixel below
            
    def draw_rect(self,pos1,pos2):
        self.draw_line((pos1[0],pos2[1]),(pos2[0],pos2[1]))
        self.draw_line((pos1[0],pos1[1]),(pos2[0],pos1[1]))
        self.draw_line((pos1[0],pos1[1]),(pos1[0],pos2[1]))
        self.draw_line((pos2[0],pos1[1]),(pos2[0],pos2[1]))

    def draw_circle(self,pos1,pos2):
        radius=math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)
        for i in range(360):
            angle1=math.radians(i)
            x1=math.floor(pos1[0]+radius*math.cos(angle1))
            y1=math.floor(pos1[1]+radius*math.sin(angle1))

            angle2=math.radians(i+1)
            x2=math.floor(pos1[0]+radius*math.cos(angle2))
            y2=math.floor(pos1[1]+radius*math.sin(angle2))

            self.draw_line((x1,y1),(x2,y2))
        
    def handle_event(self,event):
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if((self.state=="pen") or (self.state=="eraser")):  
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start drawing the line when the mouse button is pressed
                self.is_dragging = True
                self.start_pos = self.screen_to_array(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                # stop drawing the line when the mouse button is released
                self.is_dragging = False
                self.start_pos=None
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                # draw the line as the mouse is dragged
                end_pos = self.screen_to_array(pygame.mouse.get_pos())
                if(end_pos==None or self.start_pos==None):return
                self.draw_line(self.start_pos, end_pos)
                self.start_pos = end_pos
        elif(self.state=="fill"):
            if(event.type==pygame.MOUSEBUTTONDOWN):
                pos=event.pos
                if((pos[0]>self.positionX and pos[0]<self.positionX+self.size) and (pos[1]>self.positionY and pos[1]<self.positionY+self.size)):  
                    arval=self.screen_to_array(event.pos)
                    self.flood_fill(arval,self.pixel_array[self.maintain(arval[1]),self.maintain(arval[0])])         
        elif(self.state=="line"):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start drawing the line when the mouse button is pressed
                self.is_dragging = True
                self.start_pos = self.screen_to_array(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                # stop drawing the line when the mouse button is released
                self.is_dragging = False
                end_pos = self.screen_to_array(pygame.mouse.get_pos())               
                if(end_pos==None or self.start_pos==None):return    
                self.draw_line(self.start_pos, end_pos)
                self.start_pos=None
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                # draw the line as the mouse is dragged
                end_pos = self.screen_to_array(pygame.mouse.get_pos())
        elif(self.state=="rect"):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start drawing the line when the mouse button is pressed
                self.is_dragging = True
                self.start_pos = self.screen_to_array(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                # stop drawing the line when the mouse button is released
                self.is_dragging = False
                end_pos = self.screen_to_array(pygame.mouse.get_pos())               
                if(end_pos==None or self.start_pos==None):return    
                self.draw_rect(self.start_pos, end_pos)
                self.start_pos=None
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                # draw the line as the mouse is dragged
                end_pos = self.screen_to_array(pygame.mouse.get_pos())
            
        elif(self.state=="circle"):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start drawing the line when the mouse button is pressed
                self.is_dragging = True
                self.start_pos = self.screen_to_array(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                # stop drawing the line when the mouse button is released
                self.is_dragging = False
                end_pos = self.screen_to_array(pygame.mouse.get_pos())               
                if(end_pos==None or self.start_pos==None):return    
                self.draw_circle(self.start_pos, end_pos)
                self.start_pos=None
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                # draw the line as the mouse is dragged
                end_pos = self.screen_to_array(pygame.mouse.get_pos())
                
    
      
           
    def update(self,event):
        self.handle_event(event)
        
    
    def map_depth(self,n):
        nd=self.axis_density-n
        nd=100*nd/self.axis_density
        return int(nd)
    
    def pygame_rect(self,pos1,pos2):
        pygame.draw.line(self.screen,(28, 185, 252),(pos1[0],pos2[1]),(pos2[0],pos2[1]),self.line_width)
        pygame.draw.line(self.screen,(28, 185, 252),(pos1[0],pos1[1]),(pos2[0],pos1[1]),self.line_width)
        pygame.draw.line(self.screen,(28, 185, 252),(pos1[0],pos1[1]),(pos1[0],pos2[1]),self.line_width)
        pygame.draw.line(self.screen,(28, 185, 252),(pos2[0],pos1[1]),(pos2[0],pos2[1]),self.line_width)
        
        
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255),(self.positionX,self.positionY,self.size,self.size))
        #pygame.draw.rect(self.screen, (0,0,0),(self.positionX-self.border_width,self.positionY-self.border_width,self.size+2*self.border_width,self.size+2*self.border_width),self.border_width)
        for i in range(self.pixel_array.shape[0]):
            for j in range(self.pixel_array.shape[1]):
                    rect = pygame.Rect(self.positionX+j * self.pixel_size,self.positionY+ i * self.pixel_size, self.pixel_size, self.pixel_size)
                    pygame.draw.rect(self.screen, modify_color(self.line_color,self.map_depth(self.pixel_array[i, j])), rect)
                    
        if(self.showgrid):
            grid_density=min(50,self.axis_density)
            grid_gap=self.size/grid_density
            for i in range(grid_density):
                    pygame.draw.line(self.screen, self.grid_color, (self.positionX+(i*grid_gap),self.positionY),(self.positionX+(i*grid_gap),self.positionY+self.size), 1)
            for i in range(grid_density):
                    pygame.draw.line(self.screen, self.grid_color, (self.positionX,self.positionY+(i*grid_gap)),(self.positionX+self.size,self.positionY+(i*grid_gap)), 1)

        if (self.state=="line" and self.is_dragging and (self.start_pos!=None)):
            mx,my=pygame.mouse.get_pos()
            draw_pos=self.array_to_screen(self.start_pos)
            pygame.draw.line(self.screen, (28, 185, 252), draw_pos,(mx,my), self.line_width)

        if (self.state=="rect" and self.is_dragging and (self.start_pos!=None)):
            mx,my=pygame.mouse.get_pos()
            draw_pos=self.array_to_screen(self.start_pos)
            self.pygame_rect(draw_pos,(mx,my))

        if (self.state=="circle" and self.is_dragging and (self.start_pos!=None)):
            mx,my=pygame.mouse.get_pos()
            draw_pos=self.array_to_screen(self.start_pos)
            pygame.draw.circle(self.screen, (28, 185, 252), draw_pos, int(math.sqrt((mx-draw_pos[0])**2+(my-draw_pos[1])**2)), self.line_width)
        
        
        

        
if __name__ =="__main__":
    pygame.init()
    screenlengthx=600
    screenlengthy=600
    screen=pygame.display.set_mode((screenlengthx,screenlengthy))


    board=drawingboard(screen,(50,50))
        
    running=True
    while running:
        screen.fill((55,55,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            board.handle_event(event)
            
        board.draw()
        

        pygame.display.update()
                        