import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class explorer(updater):
    def __init__(self,screen,pos,width,height,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = height
        
        super().__init__()
        
    def update(self,event):
       pass
        
    
    def draw(self):
       pass
        
    
        