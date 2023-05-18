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
    def __init__(self,screen,pos,width,height=28,color=(255,255,255),sliderval=100):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.color = color
        self.height = height
        
        self.operation="pen"
        
        self.slider1Color_bg=(228, 201, 255)
        self.slider1Color=(147, 132, 209)
        
        self.slider2Color_bg=(228, 201, 255)
        self.slider2Color=(147, 132, 209)
        
        self.button_color=(204, 232, 252)
        self.button_color2=(222, 252, 204)

        self.line_spacing=4
        
        self.slider1Text=textbox(screen,(0,pos[1],400,25),color=self.slider1Color_bg,text_size=20)
        self.slider1=slider(screen,(15,pos[1]+35),300,10,max_value=(sliderval//10) +1,min_value=0,default_value=1,color=self.slider1Color)
        
        self.slider2Text=textbox(screen,(400,pos[1],400,25),color=self.slider2Color_bg,text_size=20)        
        self.slider2=slider(screen,(415,pos[1]+35),300,10,max_value=sliderval,min_value=0,default_value=sliderval,color=self.slider2Color)
        
        self.pen_button=state_button(screen,position=(50+self.line_spacing,102),size=(80,24),text="Brush",color=self.button_color2,instance=False,corner_radius=10,zoom=0.8 ,text_color=(0, 65, 112))
        self.pen_button.state=True
        
        
        self.line_button=state_button(screen,position=(370+5*self.line_spacing,102),size=(80,24),text="Line",color=self.button_color,instance=False,corner_radius=10,zoom=0.8,text_color=(0, 65, 112))
        self.line_button.state=False

        self.rect_button=state_button(screen,position=(210+3*self.line_spacing,102),size=(80,24),text="Rect",color=self.button_color,instance=False,corner_radius=10,zoom=0.8,text_color=(0, 65, 112))
        self.rect_button.state=False

        self.circle_button=state_button(screen,position=(290+4*self.line_spacing,102),size=(80,24),text="Circle",color=self.button_color,instance=False,corner_radius=10,zoom=0.8,text_color=(0, 65, 112))
        self.circle_button.state=False


        
        self.fill_button=state_button(screen,position=(130+2*self.line_spacing,102),size=(80,24),text="Fill",color=self.button_color2,instance=False,corner_radius=10,zoom=0.8,text_color=(0, 65, 112))
        self.fill_button.state=False
        
        self.grid_button=state_button(screen,position=(450+6*self.line_spacing,102),size=(80,24),text="Grid",color=(199, 255, 231),instance=False,corner_radius=10,zoom=0.8,text_color=(1, 64, 37))
        self.grid_button.state=False
        
        self.select_text=textbox(screen,(580,100,120,30),color=(255, 238, 179),text_size=20,text_color=(158, 111, 33),rotation=0)
        self.undo_button=button(screen,position=(710,102),size=(80,24),text="Undo",color=(52, 235, 198),instance=False,corner_radius=10,zoom=0.8,text_color=(1, 64, 37))
        
        self.button_obj={
            "pen":self.pen_button,
            "line":self.line_button,
            "fill":self.fill_button,
            "rect":self.rect_button,
            "circle":self.circle_button
        }
        self.undo_state=False;
        super().__init__()
        
    def update(self,event):
        self.slider1Text.update(event)
        self.slider1.update(event)
        self.slider2Text.update(event)
        self.slider2.update(event)
        
        self.grid_button.update(event)
        self.undo_state=self.undo_button.update(event)
        
        
        for i in self.button_obj.keys():
            currentState=self.button_obj[i].update(event)
            if currentState:
                self.operation=i
                for j in self.button_obj.keys():
                    if j!=i:
                        self.button_obj[j].state=False
            
    def get_value(self,slider):
        if(slider==1):
            return self.slider1.get_value()
        elif(slider==2):
            return self.slider2.get_value()
        
    def get_operation(self):
        return self.operation
    
    def get_grid(self):
        return self.grid_button.state
    
    def get_undo(self):
        return self.undo_state
        

    def draw(self):
        pygame.draw.rect(self.screen,(self.color),(self.pos[0],self.pos[1],self.width,self.height))
        
        self.slider1Text.draw("WIDTH")
        pygame.draw.rect(self.screen,self.slider1Color_bg,(0,self.pos[1]+25,400,40))
        self.slider1.draw()
        
        self.slider2Text.draw("DEPTH")
        pygame.draw.rect(self.screen,self.slider2Color_bg,(400,self.pos[1]+25,400,40))
        self.slider2.draw()
        
        
        self.pen_button.draw()
        self.grid_button.draw()
        self.fill_button.draw()
        self.line_button.draw()
        self.rect_button.draw()
        self.circle_button.draw()
        self.undo_button.draw()
        text=self.operation.upper()+" SELECTED "
        self.select_text.draw(text)
        pygame.draw.line(self.screen,(117, 52, 128),(self.pos[0]+400-1,self.pos[1]+10),(self.pos[0]+400-1,self.pos[1]+self.height-40),2)
        pygame.draw.line(self.screen,(117, 52, 128),(0,128),(self.width,128),1)
        pygame.draw.line(self.screen,(117, 52, 128),(0,35),(self.width,35),1)
        
        
        