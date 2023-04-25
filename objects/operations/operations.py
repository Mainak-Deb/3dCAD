import pygame
import math

def display_text(surface, text, font, color, position):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center=position
    surface.blit(text_obj, text_rect)
       
def modify_color(color,value):
        return (min(int(color[0]*value/100),255),min(int(color[1]*value/100),255),min(int(color[2]*value/100),255))

def calculate_darkness(rgb_tuple):
    r, g, b = rgb_tuple
    darkness = 1 - (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return darkness

def calculate_text_color(rgb_tuple):
    darkness=calculate_darkness(rgb_tuple)
    if(darkness > 0.5):return (255,255,255)
    else:return (0,0,0)
    
def rotated_text(text, font, angle):
    # render the text onto a surface
    text_surface = font.render(text, True, (255, 255, 255))
    # get the size of the surface
    surface_size = text_surface.get_size()
    # calculate the size of the rotated surface
    rotated_size = (int(surface_size[1] * math.sin(math.radians(angle))) + surface_size[0], int(surface_size[1] * math.cos(math.radians(angle))) + surface_size[1])
    # create the rotated surface
    rotated_surface = pygame.Surface(rotated_size, pygame.SRCALPHA)
    # rotate the surface by the specified angle
    rotated_surface = pygame.transform.rotate(rotated_surface, angle)
    # blit the text onto the rotated surface
    rotated_surface.blit(text_surface, (0, 0))
    return rotated_surface