import pygame
import sys

#custom buttons
import objects

# create a Pygame window and manager
pygame.init()
window_size = (640, 480)
window = pygame.display.set_mode(window_size)

# create a button and add it to the manager




# main game loop
while True:
    # handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    # update the GUI manager

    # draw the GUI elements and update the Pygame display
    window.fill((255, 255, 255))
    pygame.display.update()
