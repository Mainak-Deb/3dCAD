import time
import pygame,sys,random
from pygame.locals import *
import math




class button:
    def __init__(self,screen,positionx,positiony,width,height,colour,font,text):
        self.screen=screen
        self.positionx=positionx
        self.positiony=positiony
        self.width=width
        self.height=height
        self.colour=colour
        self.font=font
        self.text=text
        self.state=False;

    def draw(self):
        if(self.state):
            self.colour=(0,255,0)
        else:
            self.colour=(255,255,255)
        pygame.draw.rect(self.screen,self.colour,(self.positionx,self.positiony,self.width,self.height))
        pygame.draw.rect(self.screen,(0,0,0),(self.positionx,self.positiony,self.width,self.height),4)
        text=self.font.render(self.text,True,(0,0,0))
        self.screen.blit(text,(self.positionx+self.width/2-text.get_width()/2,self.positiony+self.height/2-text.get_height()/2))

    def isHover(self):
        mousex,mousey=pygame.mouse.get_pos()
        if( mousex>=self.positionx and mousex<=self.positionx+self.width and mousey>=self.positiony and mousey<=self.positiony+self.height):
            return True
        else:
            return False