import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class toolbar(updater):
    def __init__(self,screen,pos,width,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = 28
        self.homebutton=button(screen,"Home",(0,0),(80,self.height),(200,200,200),instance=False,corner_radius=0)
        self.newbutton=button(screen,"New",(80,0),(80,self.height),(200,200,200),instance=False,corner_radius=0)
        self.openbutton=button(screen,"Open",(160,0),(80,self.height),(200,200,200),instance=False,corner_radius=0)
        self.savebutton=button(screen,"Save",(240,0),(80,self.height),(200,200,200),instance=False,corner_radius=0)
        super().__init__()
        
    def update(self,event):
        self.homebutton.update(event)
        self.newbutton.update(event)
        self.openbutton.update(event)
        self.savebutton.update(event)
        
    
    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        self.homebutton.draw()
        self.newbutton.draw()
        self.openbutton.draw()
        self.savebutton.draw()
        
    
        