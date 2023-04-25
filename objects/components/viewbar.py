import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater
from objects.components.button import button,state_button,icon_button
from objects.components.slider import slider
from objects.components.textbox import textbox

class viewbar(updater):
    def __init__(self,screen,pos,width,height=28,color=(255,255,255)):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = height
        
        self.operation="pen"
        
        self.slider1Color_bg=(187, 214, 184)
        self.slider1Color=(148, 175, 159)
        
        self.slider2Color_bg=(174, 226, 255)
        self.slider2Color=(147, 198, 231)
        
        self.slider1Text=textbox(screen,(0,pos[1],400,30),color=self.slider1Color_bg,text_size=20)
        self.slider1=slider(screen,(15,pos[1]+40),300,12,max_value=10,min_value=0,default_value=5,color=self.slider1Color)
        
        self.slider2Text=textbox(screen,(400,pos[1],400,30),color=self.slider2Color_bg,text_size=20)        
        self.slider2=slider(screen,(415,pos[1]+40),300,12,max_value=100,min_value=0,default_value=50,color=self.slider2Color)
        
        self.pen_button=state_button(screen,position=(50,100),size=(80,30),text="Pen",color=(213, 126, 247),instance=False,corner_radius=0)
        self.pen_button.state=True
        
        self.eraser_button=state_button(screen,position=(130,100),size=(80,30),text="Eraser",color=(213, 126, 247),instance=False,corner_radius=0)
        self.eraser_button.state=False
        
        self.select_text=textbox(screen,(210,100,140,30),color=(255, 238, 179),text_size=20,text_color=(158, 111, 33),rotation=0)
        
        super().__init__()
        
    def update(self,event):
        self.slider1Text.update(event)
        self.slider1.update(event)
        self.slider2Text.update(event)
        self.slider2.update(event)
        if(self.pen_button.update(event)):
            self.eraser_button.state=False
            self.operation="pen"
        if(self.eraser_button.update(event)):
            self.pen_button.state=False
            self.operation="eraser"
        
            
    def get_value(self,slider):
        if(slider==1):
            return self.slider1.get_value()
        elif(slider==2):
            return self.slider2.get_value()
        
    def get_operation(self):
        return self.operation

    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        
        self.slider1Text.draw("WIDTH")
        pygame.draw.rect(self.screen,self.slider1Color_bg,(0,self.pos[1]+30,400,40))
        self.slider1.draw()
        
        self.slider2Text.draw("DEPTH")
        pygame.draw.rect(self.screen,self.slider2Color_bg,(400,self.pos[1]+30,400,40))
        self.slider2.draw()
        
        self.pen_button.draw()
        self.eraser_button.draw()
        self.select_text.draw(self.operation.upper()+" SELECTED")
        
        