import pygame
from pygame.locals import *

import sys
sys.path.append('./')

import objects




def page1(screen,screenlengthx,screenlengthy): 
    toolbar=objects.components.toolbar(screen,(0,0),screenlengthx,28)
    viewbar=objects.components.viewbar(screen,(0,28),screenlengthx,102,color=(200,200,200))
    drawingbox=objects.components.drawingboard(screen,(50,129),size=600,axis_density=100) 
    
    sidebar=objects.components.sidebar(screen,(650,129),150,600,color=(253, 244, 245))
     
    sidetext=objects.components.textbox(screen,(0,129,50,600),color=(255, 238, 179),text_size=40,text_color=(158, 111, 33),rotation=90)
    
    #value texts will appear here
    widthValueText=objects.components.textbox(screen,(660,490,130,40),color=(228, 220, 207),text_size=30,text_color=(158, 111, 33))
    widthValue=objects.components.textbox(screen,(660,530,130,40),color=(249, 245, 235),text_size=30,text_color=(158, 111, 33))
    
    depthValueText=objects.components.textbox(screen,(660,590,130,40),color=(228, 220, 207),text_size=30,text_color=(158, 111, 33))
    depthValue=objects.components.textbox(screen,(660,630,130,40),color=(249, 245, 235),text_size=30,text_color=(158, 111, 33))
    
    
    
    running=True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            objects.components.updater.update(event)
        objects.components.updater.draw()
        sidetext.draw(sidebar.get_selected()+" view")
        
        widthValueText.draw("WIDTH")
        widthValue.draw(str(viewbar.get_value(slider=1)))
        depthValueText.draw("DEPTH")
        depthValue.draw(str(viewbar.get_value(slider=2)))
        
        drawingbox.set_width(viewbar.get_value(slider=1))   
        
        
        pygame.display.update()
                        
