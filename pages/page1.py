import pygame
from pygame.locals import *

import sys
sys.path.append('./')

import objects

def page1(screen,screenlengthx,screenlengthy): 
    toolbar=objects.components.toolbar(screen,(0,0),screenlengthx)
    running=True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            objects.components.updater.update(event)
        objects.components.updater.draw()
        pygame.display.update()
                        
