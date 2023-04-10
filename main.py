import pygame
from pygame.locals import *
import sys
sys.path.append('./')
import objects
import pages


pygame.init()
screenlengthx=800
screenlengthy=600
screen=pygame.display.set_mode((screenlengthx,screenlengthy))


pages.page1(screen,screenlengthx,screenlengthy)