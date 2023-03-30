import pygame

def display_text(surface, text, font, color, position):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center=position
    surface.blit(text_obj, text_rect)

def rounded_rect(screen,color,rect):
    rect_x,rect_y,rect_width,rect_height = rect
    corner_radius = rect_height//2
    pygame.draw.rect(screen, color, (rect_x + corner_radius, rect_y, rect_width - 2*corner_radius, rect_height))
    pygame.draw.rect(screen, color, (rect_x, rect_y + corner_radius, rect_width, rect_height - 2*corner_radius))

    # Draw circles to create rounded edges
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + rect_height - corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + rect_height - corner_radius), corner_radius)




class Slider:
    def __init__(self, screen, x, y, width, height, min_value=0, max_value=100, default_value=50, color=(255, 92, 206), knob_color=(255, 92, 206),border_color=(255,255,255),border_width=10):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value_range = max_value - min_value
        self.value = default_value
        self.color = color
        self.knob_color = knob_color
        self.border_color = border_color
        self.border_width = border_width
        self.knob_width = int(height*2)
        self.knob_height = int(height*2)
        self.knob_x = self.value_to_position(default_value) - self.knob_width // 2
        self.knob_y = self.y
        self.dragging = False
        self.font = pygame.font.Font(None, 20)

    def draw(self):
        # Draw the slider background
        self.value = int((self.position_to_value(self.knob_x + self.knob_width // 2)-5)/90*100)
        rounded_rect(self.screen, self.border_color, (self.x-self.border_width, self.y-self.border_width, self.width+(2*self.border_width)+60, self.height+(2*self.border_width)))
        
        rounded_rect(self.screen, (200,200,200), (self.x, self.y, self.width, self.height))
        rounded_rect(self.screen, self.color, (self.x, self.y, self.knob_x-self.x+self.knob_width, self.height))

        # Draw the knob
        rounded_rect(self.screen, self.knob_color, (self.knob_x, self.knob_y-self.height//2, self.knob_width, self.knob_height))
        rounded_rect(self.screen,  self.knob_color, (self.x+self.width+10, self.knob_y-self.height//2, 50, self.knob_height))
        
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
            self.knob_x = max(self.x, min(event.pos[0] - self.knob_width // 2, self.x + self.width - self.knob_width))
            self.value = self.position_to_value(self.knob_x + self.knob_width // 2)

    def position_to_value(self, position):
        # Convert the knob position to a value in the range
        position_normalized = (position - self.x) / self.width
        return self.min_value + position_normalized * self.value_range

    def value_to_position(self, value):
        # Convert a value to a knob position on the slider
        value_normalized = (value - self.min_value) / self.value_range
        return round(self.x + value_normalized * self.width)

    def update(self,event=None):
        if(event!=None):self.handle_event(event)
        self.draw()
        

if __name__ == '__main__':
    # Initialize Pygame
    pygame.init()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set the dimensions of the screen and the font
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    FONT_SIZE = 32

    # Create the Pygame window and set the font
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont(None, FONT_SIZE)

    slider = Slider(screen,100, 100, 200, 10)

    # Game loop
    running = True
    while running:
        screen.fill((0,0,0))
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            slider.update(event)

        slider.update()
        # Update the Pygame display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()