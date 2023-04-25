import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button

class sidebar(updater):
    '''
    This sidebar class is used to create a sidebar object that can be used to display buttons and other components.
    This will return the state state of the whole software
    '''
    def __init__(self,screen,pos,width,height=400,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height =height
        self.button_height=50
        self.button_spacing=0
        self.state="Top"
        
        self.topButton=state_button(screen,"Top",(pos[0],pos[1]),(self.width,self.button_height),(200, 255, 212),instance=False,corner_radius=0,border_width=1)
        self.bottomButton=state_button(screen,"Bottom",(pos[0],pos[1]+self.button_height+self.button_spacing),(self.width,self.button_height),(253, 253, 189),instance=False,corner_radius=0,border_width=1)
        self.frontButton=state_button(screen,"Front",(pos[0],pos[1]+2*(self.button_height+self.button_spacing)),(self.width,self.button_height),(200, 255, 212),instance=False,corner_radius=0,border_width=1)
        self.backButton=state_button(screen,"Back",(pos[0],pos[1]+3*(self.button_height+self.button_spacing)),(self.width,self.button_height),(253, 253, 189),instance=False,corner_radius=0,border_width=1)
        self.leftButton=state_button(screen,"Left",(pos[0],pos[1]+4*(self.button_height+self.button_spacing)),(self.width,self.button_height),(200, 255, 212),instance=False,corner_radius=0,border_width=1)
        self.rightButton=state_button(screen,"Right",(pos[0],pos[1]+5*(self.button_height+self.button_spacing)),(self.width,self.button_height),(253, 253, 189),instance=False,corner_radius=0,border_width=1)
        self.sidebar_buttons={
            "Top":self.topButton,
            "Bottom":self.bottomButton,
            "Front":self.frontButton,
            "Back":self.backButton,
            "Left":self.leftButton,
            "Right":self.rightButton
        }        
        super().__init__()
        
    def update(self,event):
        for i in self.sidebar_buttons.keys():
            currentState=self.sidebar_buttons[i].update(event)
            if currentState:
                self.state=i
                for j in self.sidebar_buttons.keys():
                    if j!=i:
                        self.sidebar_buttons[j].state=False


    def get_selected(self):
        return self.state

    
    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        self.topButton.draw()
        self.bottomButton.draw()
        self.frontButton.draw()
        self.backButton.draw()
        self.leftButton.draw()
        self.rightButton.draw()
        pygame.draw.rect(self.screen,(177, 175, 255),(self.pos[0]+4,self.pos[1]+350+4,self.width-8,200))


        