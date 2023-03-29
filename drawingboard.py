import time
import pygame,sys,random
from pygame.locals import *
import math
import numpy as np
from numpy import ones,vstack
from numpy.linalg import lstsq




class drawingboard:
    def __init__(self,screen,positionx,positiony,width):
        self.screen=screen
        self.positionx=positionx
        self.positiony=positiony
        self.width=width
        self.window_size=(width,width)
        self.colour=(255,255,255)
        self.pixel_size=self.width//100
        self.state=False
        self.mouseQueue=[]
        self.line_width = 1
        self.pixel_array = np.zeros((self.window_size[1] // self.pixel_size, 
                                     self.window_size[0] // self.pixel_size), dtype=bool)
        self.is_dragging = False
        self.start_pos=None
        self.line_color = (0, 0, 255)
        
    def maintain(self,a):
        if(a<0):return 0;
        elif(a>=self.width):return self.width-1
        else:return a
        
    # create a function to convert screen coordinates to array indices
    def screen_to_array(self,pos):
        pos=(self.maintain(pos[0]-self.positionx),self.maintain(pos[1]-self.positiony))
        return pos[0] // self.pixel_size, pos[1] // self.pixel_size

    # create a function to handle mouse events
    def handle_events(self,eventname):    
            if eventname=="MOUSEBUTTONDOWN":
                # start drawing the line when the mouse button is pressed
                self.is_dragging = True
                self.start_pos = self.screen_to_array(pygame.mouse.get_pos())  

            elif eventname=="MOUSEBUTTONUP":
                # stop drawing the line when the mouse button is released
                self.is_dragging = False
                self.start_pos=None
            elif eventname=="MOUSEMOTION" and self.is_dragging:
                end_pos = self.screen_to_array(pygame.mouse.get_pos())
                self.draw_line(self.start_pos, end_pos,2)
                self.start_pos = end_pos
                
            # print(self.is_dragging)
    def draw_line(self,start_pos, end_pos,linewidth):
        # use Bresenham's line algorithm to find the pixels to draw
        if(start_pos==None):
            return
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


    def draw_pixels(self):
        # pygame.draw.rect(self.screen, (255,255,255), (self.positionx,self.positiony,self.width,self.width))
        for i in range(self.pixel_array.shape[0]):
            for j in range(self.pixel_array.shape[1]):
                rect = pygame.Rect(self.positionx+j * self.pixel_size, self.positiony+i * self.pixel_size, self.pixel_size, self.pixel_size)
                if self.pixel_array[i, j]:
                    pygame.draw.rect(self.screen, self.line_color, rect)
                else:
                    pygame.draw.rect(self.screen, (255,255,255), rect)
                    
    def update(self,eventname=None):
        self.handle_events(eventname);
        self.draw_pixels();
        
