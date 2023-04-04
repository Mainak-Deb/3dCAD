import pygame
import sys
sys.path.append('./')
from objects.operations import *


def hoverable_circle(window_surface, circle_color, circle_position, circle_radius):
        mouse_pos = pygame.mouse.get_pos()
        if ((mouse_pos[0] - circle_position[0]) ** 2 + (mouse_pos[1] - circle_position[1]) ** 2) <= circle_radius ** 2:
            color = modify_color(circle_color,85) 
        else:
           color =circle_color
        pygame.draw.circle(window_surface, color, circle_position, circle_radius)
        