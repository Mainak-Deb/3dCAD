import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class toolbar(updater):
    def __init__(self,screen,pos,width,height=28,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = height
        self.homebutton=button(screen,"Home",(0,0),(80,self.height),self.color,instance=False,corner_radius=0,border_width=1)
        self.newbutton=button(screen,"New",(80,0),(80,self.height),self.color,instance=False,corner_radius=0,border_width=1)
        self.openbutton=button(screen,"Open",(160,0),(80,self.height),self.color,instance=False,corner_radius=0,border_width=0)
        self.savebutton=button(screen,"Save",(240,0),(80,self.height),self.color,instance=False,corner_radius=0,border_width=0)
        super().__init__()
        self.state={
            "home":False,
            "new":False,
            "open":False,
            "save":False
        }
        
    def update(self,event):
        self.state["home"]=self.homebutton.update(event)
        self.state["new"]=self.newbutton.update(event)
        self.state["open"]=self.openbutton.update(event)
        self.state["save"]=self.savebutton.update(event)
        
        
    def get_state(self,value):
        return self.state[value]
    
    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        self.homebutton.draw()
        self.newbutton.draw()
        self.openbutton.draw()
        self.savebutton.draw()
        
    
        