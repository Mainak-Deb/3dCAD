import pygame
import pygame
import sys
sys.path.append('./')
from objects.operations import *


def rounded_rect(screen,color=(255,255,255),rect=(0,0,0,0)):
    rect_x,rect_y,rect_width,rect_height = rect
    corner_radius = rect_height//2
    pygame.draw.rect(screen, color, (rect_x + corner_radius, rect_y, rect_width - 2*corner_radius, rect_height))
    pygame.draw.rect(screen, color, (rect_x, rect_y + corner_radius, rect_width, rect_height - 2*corner_radius))

    # Draw circles to create rounded edges
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + rect_height - corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + rect_height - corner_radius), corner_radius)
