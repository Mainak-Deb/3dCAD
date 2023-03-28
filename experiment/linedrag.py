import pygame

# initialize pygame
pygame.init()

# set the window size
window_size = (800, 600)

# create the window
screen = pygame.display.set_mode(window_size)

# set the caption
pygame.display.set_caption("Line Drawing Example")

# set the background color
background_color = (255, 255, 255)

# set the line color
line_color = (0, 0, 255)

# set the line width
line_width = 3

# create a list to store the points of the line
line_points = []

# create a boolean variable to keep track of whether the mouse is being dragged
is_dragging = False

# create a function to handle mouse events
def handle_events():
    global is_dragging, line_points
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # start a new line when the mouse button is pressed
            is_dragging = True
            line_points = [event.pos]
        elif event.type == pygame.MOUSEBUTTONUP:
            # end the current line when the mouse button is released
            is_dragging = False
            line_points = []
        elif event.type == pygame.MOUSEMOTION and is_dragging:
            # add points to the line as the mouse is dragged
            line_points.append(event.pos)

# create a function to draw the line
def draw_line():
    if len(line_points) > 1:
        pygame.draw.lines(screen, line_color, False, line_points, line_width)

# create the main game loop
def game_loop():
    while True:
        # handle events
        handle_events()
        
        # clear the screen
        screen.fill(background_color)
        
        # draw the line
        draw_line()
        
        # update the screen
        pygame.display.update()

# start the game loop
game_loop()
