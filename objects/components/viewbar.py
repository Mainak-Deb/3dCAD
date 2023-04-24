import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class viewbar(updater):
    def __init__(self,screen,pos,width,height=28,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = height
        
        super().__init__()
        
    def update(self,event):
        ...
        
    
    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        