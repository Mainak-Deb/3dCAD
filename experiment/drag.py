import pygame

# initialize pygame
pygame.init()

# set the window size
window_size = (800, 600)

# create the window
screen = pygame.display.set_mode(window_size)

# set the caption
pygame.display.set_caption("Mouse Drag Example")

# set the background color
background_color = (255, 255, 255)

# set the circle color
circle_color = (255, 0, 0)

# set the circle radius
circle_radius = 50

# set the starting position of the circle
circle_position = (window_size[0] // 2, window_size[1] // 2)

# create a boolean variable to keep track of whether the mouse is being dragged
is_dragging = False

# create a function to handle mouse events
def handle_events():
    global is_dragging, circle_position
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is over the circle
            if (event.pos[0] - circle_position[0])**2 + (event.pos[1] - circle_position[1])**2 <= circle_radius**2:
                is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            is_dragging = False
        elif event.type == pygame.MOUSEMOTION and is_dragging:
            # update the position of the circle based on the mouse movement
            circle_position = event.pos

# create a function to draw the circle
def draw_circle():
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

# create the main game loop
def game_loop():
    while True:
        # handle events
        handle_events()
        
        # clear the screen
        screen.fill(background_color)
        
        # draw the circle
        draw_circle()
        
        # update the screen
        pygame.display.update()

# start the game loop
game_loop()
