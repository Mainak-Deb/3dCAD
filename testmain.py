import pygame
from pygame.locals import *

import sys
sys.path.append('./')

import objects


pygame.init()
screenlengthx=800
screenlengthy=600
screen=pygame.display.set_mode((screenlengthx,screenlengthy))


button=objects.components.button(screen,"Touch me",(screenlengthx//2-100,screenlengthy//2),(100,50),(232, 160, 191))
iButton=objects.components.icon_button(screen,"images/search.png",(screenlengthx//2-250,screenlengthy//2),(100,50),(221, 255, 187))
sButton=objects.components.state_button(screen,"Click me",(screenlengthx//2+100,screenlengthy//2),(100,50),(178, 164, 255))

    
running=True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        objects.components.button.update(event)
        
    objects.components.button.draw()
    

    pygame.display.update()
                    