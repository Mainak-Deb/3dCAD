import pygame

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
    