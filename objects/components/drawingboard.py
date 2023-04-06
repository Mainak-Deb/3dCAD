import pygame
from pygame.locals import *
import numpy as np
import math

class drawingBoard:
    def __init__(self, screen, position, size=400,color=(0,0,255),axis_density=100):
        self.screen = screen
        self.positionX=position[0]
        self.positionY=position[1]
        self.size=size
        self.pixel_array = np.zeros((size, size), dtype=bool)
        self.pixel_size = size//axis_density
        self.is_dragging = False
        self.start_pos = None
        self.line_width = 1
        self.line_color = (0,0, 255)
        
    
    def screen_to_array(self, pos):
        return (pos[0]-self.positionX) // self.pixel_size,( pos[1]-self.positionY) // self.pixel_size

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
            self.pixel_array[y0, x0] = True
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
    
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255),(self.positionX,self.positionY,self.size,self.size))
        for i in range(self.pixel_array.shape[0]):
            for j in range(self.pixel_array.shape[1]):
                if self. pixel_array[i, j]:
                    rect = pygame.Rect(self.positionX+j * self.pixel_size,self.positionY+ i * self.pixel_size, self.pixel_size, self.pixel_size)
                    pygame.draw.rect(self.screen, self.line_color, rect)


    def handle_events(self,event):
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                self.draw_line(self.start_pos, end_pos)
                self.start_pos = end_pos
        
if __name__ =="__main__":
    pygame.init()
    screenlengthx=1400
    screenlengthy=600
    screen=pygame.display.set_mode((screenlengthx,screenlengthy))


    board=drawingBoard(screen,(50,50))
        
    running=True
    while running:
        screen.fill((55,55,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            board.handle_events(event)
            
        board.draw()
        

        pygame.display.update()
                        