import pygame
import numpy as np
import math

# initialize pygame
pygame.init()

# set the window size and pixel size
window_size = (800, 600)
pixel_size = 4

# create the window
screen = pygame.display.set_mode(window_size)

# set the caption
pygame.display.set_caption("Line Drawing Example")

# set the background color
background_color = (255, 255, 255)

# set the line color
line_color = (0, 0, 255)

# set the line width
line_width = 4

# create a bit array to represent the pixels
pixel_array = np.zeros((window_size[1] // pixel_size, window_size[0] // pixel_size), dtype=bool)

# create a boolean variable to keep track of whether the mouse is being dragged
is_dragging = False
start_pos=None

# create a function to convert screen coordinates to array indices
def screen_to_array(pos):
    return pos[0] // pixel_size, pos[1] // pixel_size

# create a function to handle mouse events
def handle_events():
    global is_dragging,start_pos
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # start drawing the line when the mouse button is pressed
            is_dragging = True
            start_pos = screen_to_array(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            # stop drawing the line when the mouse button is released
            is_dragging = False
            start_pos=None
        elif event.type == pygame.MOUSEMOTION and is_dragging:
            # draw the line as the mouse is dragged
            end_pos = screen_to_array(pygame.mouse.get_pos())
            draw_line(start_pos, end_pos)
            start_pos = end_pos
# create a function to draw a line between two points
# create a function to draw a line between two points

def bresenham_line_algo(start_pos, end_pos):
    global pixel_array
    if(start_pos==None):return
    x0, y0 = start_pos
    x1, y1 = end_pos
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy
    while True:
        # set the pixel to True
        pixel_array[y0, x0] = True
        # check if we've reached the end of the line
        if x0 == x1 and y0 == y1:
            break
        # calculate the next pixel to draw
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def angle_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    angle = math.atan2(y2-y1, x2-x1)
    angle=-1* math.degrees(angle)
    if(angle < 0):return 360+angle
    else:return angle
    
    
    
def draw_line(start_pos, end_pos):
    global line_width
    bresenham_line_algo(start_pos, end_pos)
    angle=angle_between_points(start_pos,end_pos)
    print(angle)
    if((135<angle<225) or (45>angle) or (angle>270)):
        print("horizontal")
        for i in range(line_width):
            modified_start_pos = (start_pos[0],start_pos[1]-i)
            modified_end_pos=(end_pos[0],end_pos[1]-i)
            bresenham_line_algo(modified_start_pos, modified_end_pos)   
    else:
        print("vertical")
        for i in range(line_width):
            modified_start_pos = (start_pos[0]-i,start_pos[1])
            modified_end_pos=(end_pos[0]-i,end_pos[1])
            bresenham_line_algo(modified_start_pos, modified_end_pos) 
        
    
    
    

# create a function to draw the pixels on the screen
def draw_pixels():
    for i in range(pixel_array.shape[0]):
        for j in range(pixel_array.shape[1]):
            if pixel_array[i, j]:
                rect = pygame.Rect(j * pixel_size, i * pixel_size, pixel_size, pixel_size)
                pygame.draw.rect(screen, line_color, rect)

# create the main game loop
def game_loop():
    while True:
        # handle events
        handle_events()
        
        # clear the screen
        screen.fill(background_color)
        
        # draw the pixels
        draw_pixels()
        
        # update the screen
        pygame.display.update()

# start the game
game_loop()
