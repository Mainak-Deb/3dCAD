import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class textbox():
    def __init__(self,screen,rect:tuple,color=(255,255,255),rotation=0,text_size=20,text_color=(0,0,0)):
        self.screen = screen
        self.rect = rect
        self.color = color
        self.font=pygame.font.Font(None, text_size)   
        self.rotation = rotation
        self.text_color = text_color
        
    def update(self,event):
       ...

    
    def draw(self,text):
        pygame.draw.rect(self.screen,(self.color),self.rect)
        text_surface = self.font.render(text, True, self.text_color)
        text_surface=pygame.transform.rotate(text_surface, self.rotation)
        text_rect = text_surface.get_rect()
        # Center the rectangle on the screen
        text_rect.center = (self.rect[0]+self.rect[2]//2,self.rect[1]+self.rect[3]//2)
        
        self.screen.blit(text_surface,text_rect)


        