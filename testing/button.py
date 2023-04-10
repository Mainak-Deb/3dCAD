import pygame
from operations import *

class button:
    def __init__(self,surface, text, position, size, color=(150,150,150),text_color=(0,0,0),corner_radius=10,border_width=1):
        self.surface = surface
        self.text = text
        self.font = pygame.font.Font(None, int(size[1]*0.5))
        self.text_surface = self.font.render(self.text, True, BLACK)
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = modify_color(color,80)
        self.corner_radius = corner_radius
        self.rect = pygame.Rect(*position, *size)
        self.hovered = False
        self.border_width=border_width
        self.border_color=modify_color(color,20)
        self.text_color = text_color
        self.state=False

    def draw(self):
        # Draw the button on the given surface
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(self.surface, color, self.rect, border_radius=self.corner_radius)
        pygame.draw.rect(self.surface, self.border_color, self.rect, border_radius=self.corner_radius,width=self.border_width)
        self.surface.blit(self.text_surface, (self.position[0] + self.size[0] // 2 - self.text_surface.get_width() // 2, self.position[1] + self.size[1] // 2 - self.text_surface.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse is hovering over the button
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            # Handle the button click event
            self.state=not self.state

class icon_button(button):
    def __init__(self,surface:any,iconpath:str, position:tuple, size:tuple, color:tuple=(150,150,150),text_color:tuple=(0,0,0),corner_radius:int=10,border_width:int=1):
        super().__init__(surface,None, position, size, color,text_color, corner_radius,border_width)
        self.icon= pygame.image.load(iconpath).convert_alpha()
        
    def draw(self):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(self.surface, color, self.rect, border_radius=self.corner_radius)
        pygame.draw.rect(self.surface, (0,0,0), self.rect, border_radius=self.corner_radius,width=self.border_width)
        self.surface.blit(self.icon, self.icon.get_rect(center = self.rect.center))
    
class state_button(button):
    def __init__(self,surface:any,text:str, position:tuple, size:tuple, color:tuple=(150,150,150),text_color:tuple=(0,0,0),corner_radius:int=10,border_width:int=1):
        super().__init__(surface,text, position, size, color,text_color, corner_radius,border_width)
        self.state_color=modify_color(color,70)
        
    def draw(self):
        color=self.state_color if self.state else self.color
        if(self.hovered):color=self.hover_color
        # color = self.hover_color if self.hovered else self.state_color
        pygame.draw.rect(self.surface, color, self.rect, border_radius=self.corner_radius)
        pygame.draw.rect(self.surface, (0,0,0), self.rect, border_radius=self.corner_radius,width=self.border_width)
        self.surface.blit(self.text_surface, (self.position[0] + self.size[0] // 2 - self.text_surface.get_width() // 2, self.position[1] + self.size[1] // 2 - self.text_surface.get_height() // 2))
   