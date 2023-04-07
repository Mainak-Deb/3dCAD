import pygame
import sys
sys.path.append('./')
from objects.operations import *
from objects.shapes import *
from objects.components.updater import updater


class slider(updater):
    def __init__(self, screen, pos, width, height, color=(255, 92, 206), min_value=0, max_value=100, default_value=50):
        self.screen = screen
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value_range = max_value - min_value
        self.value = default_value
        self.color = color
        self.knob_color = color
        self.border_color = (255,255,255)
        self.border_width = 10
        self.knob_width = int(height)
        self.knob_height = int(height)
        self.knob_x = self.value_to_position(default_value) - self.knob_width 
        self.knob_y = self.y
        self.dragging = False
        self.font = pygame.font.Font(None, 20)
        super().__init__()
        # Draw the slider background
        self.value = int(self.position_to_value(self.knob_x))
        #background of slider
        rounded_rect(self.screen, self.border_color, (self.x-self.border_width, self.y-self.border_width, self.width+(2*self.border_width)+70, self.height+(2*self.border_width)))
        #sliding bar
        rounded_rect(self.screen, (200,200,200), (self.x, self.y, self.width, self.height))
        #slide filling color
        rounded_rect(self.screen, self.color, (self.x, self.y, self.knob_x-self.x+self.knob_width, self.height))
        # Draw the knob
        hoverable_circle(self.screen, self.knob_color, (self.knob_x+self.knob_height//2, self.knob_y+self.knob_height//2), self.knob_height)
        #text updating pill
        rounded_rect(self.screen,  self.knob_color, (self.x+self.width+20, self.knob_y-self.height//2, 50, self.knob_height*2))
        
        display_text(self.screen,str(self.value),self.font,(255,255,255),(self.x+self.width+35, self.knob_y-self.height//2+10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse is clicking the knob
            if self.knob_x <= event.pos[0] <= self.knob_x + self.knob_width and self.knob_y <= event.pos[1] <= self.knob_y + self.knob_height:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Stop dragging when the mouse is released
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # Move the knob based on the mouse position while dragging
            self.knob_x = max(self.x, min(event.pos[0] - self.knob_width , self.x + self.width))
            self.value = self.position_to_value(self.knob_x + self.knob_width // 2)

    def position_to_value(self, position):
        # Convert the knob position to a value in the range
        position_normalized = (position - self.x) / self.width
        return self.min_value + int(position_normalized * self.value_range)

    def value_to_position(self, value):
        # Convert a value to a knob position on the slider
        value_normalized = (value - self.min_value) / self.value_range
        return round(self.x + value_normalized * self.width)+self.knob_width

    def update(self,event=None):
        if(event!=None):self.handle_event(event)
        
    def draw(self):
        # Draw the slider background
        self.value = int(self.position_to_value(self.knob_x))
        #background of slider
        rounded_rect(self.screen, self.border_color, (self.x-self.border_width, self.y-self.border_width, self.width+(2*self.border_width)+70, self.height+(2*self.border_width)))
        #sliding bar
        rounded_rect(self.screen, (200,200,200), (self.x, self.y, self.width, self.height))
        #slide filling color
        rounded_rect(self.screen, self.color, (self.x, self.y, self.knob_x-self.x+self.knob_width, self.height))
        # Draw the knob
        hoverable_circle(self.screen, self.knob_color, (self.knob_x+self.knob_height//2, self.knob_y+self.knob_height//2), self.knob_height)
        #text updating pill
        rounded_rect(self.screen,  self.knob_color, (self.x+self.width+20, self.knob_y-self.height//2, 50, self.knob_height*2))
        
        display_text(self.screen,str(self.value),self.font,(255,255,255),(self.x+self.width+35, self.knob_y-self.height//2+10))

        
