import time
import pygame,sys,random
from pygame.locals import *
import math
from button import button
import numpy as np
# from artboard import artboard
from drawingboard import drawingboard


pygame.init()
screenlengthx=700
screenlengthy=750
screen=pygame.display.set_mode((screenlengthx,screenlengthy))


artArr=np.zeros((100,100),dtype=bool)
artArr[0:100,0:100]=False

top=button(screen,50,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"top")
front=button(screen,150,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"front")
left=button(screen,250,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"left")
right=button(screen,350,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"right")
back=button(screen,450,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"back")
bottom=button(screen,550,50,100,50,(255,255,255),pygame.font.SysFont("Arial", 30),"bottom")


buttonArr=[top,front,left,right,back,bottom]


bitpix=drawingboard(screen,50,120,600)

running=True;
while running:
    screen.fill((150,150,150))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bitpix.update("MOUSEBUTTONDOWN")
        elif event.type == pygame.MOUSEBUTTONUP:
            bitpix.update("MOUSEBUTTONUP")
        elif event.type == pygame.MOUSEMOTION:
            bitpix.update("MOUSEMOTION")
            

    for i in range(len(buttonArr)):
        buttonArr[i].draw()
        if(buttonArr[i].isHover()):
            if(event.type==MOUSEBUTTONDOWN):
                for j in range(len(buttonArr)):
                    buttonArr[j].state=False
                buttonArr[i].state=True
    bitpix.update()
    pygame.display.update()
                    