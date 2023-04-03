import pygame


def modify_color(color,value):
        return (min(int(color[0]*value/100),255),min(int(color[1]*value/100),255),min(int(color[2]*value/100),255))


class Button:
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

class icon_button(Button):
    def __init__(self,surface:any,iconpath:str, position:tuple, size:tuple, color:tuple=(150,150,150),text_color:tuple=(0,0,0),corner_radius:int=10,border_width:int=1):
        super().__init__(surface,None, position, size, color,text_color, corner_radius,border_width)
        self.icon= pygame.image.load(iconpath).convert_alpha()
        
    def draw(self):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(self.surface, color, self.rect, border_radius=self.corner_radius)
        pygame.draw.rect(self.surface, (0,0,0), self.rect, border_radius=self.corner_radius,width=self.border_width)
        self.surface.blit(self.icon, self.icon.get_rect(center = self.rect.center))
    
class state_button(Button):
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
    

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rounded Corner Button Example")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the button
button = Button(screen,"Click me!", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50), (100, 50), RED)
iButton=icon_button(screen,"experiment\search.png",(SCREEN_WIDTH // 2 +200, SCREEN_HEIGHT // 2 - 50), (100, 50), GREEN)
sButton=state_button(screen,"Click me 2!", (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 - 50), (100, 50), GRAY)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the user closes the window
            running = False
        else:
            # Handle events on the button
            button.handle_event(event)
            iButton.handle_event(event)
            sButton.handle_event(event)

    # Draw the button and update the screen
    screen.fill(WHITE)
    
    button.draw()
    iButton.draw()
    sButton.draw()
    
    pygame.display.update()

# Quit Pygame
pygame.quit()
