import pygame
from pygame.locals import *

import sys
sys.path.append('./')

import objects




def page1(screen,screenlengthx,screenlengthy): 
    toolbar=objects.components.toolbar(screen,(0,0),screenlengthx,28)
    viewbar=objects.components.viewbar(screen,(0,28),screenlengthx,100,color=(200,200,200))
    drawingbox=objects.components.drawingboard(screen,(48,129),size=600,axis_density=100) 
    
    sidebar=objects.components.sidebar(screen,(650,129),150,600,color=(184, 232, 252))
     
    sidetext=objects.components.textbox(screen,(0,129,48,600),color=(255, 238, 179),text_size=40,text_color=(158, 111, 33),rotation=90)
    
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
        
        
        pygame.display.update()
                        
