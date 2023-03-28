import pygame
import pygame_gui
import sys

# create a Pygame window and manager
pygame.init()
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
manager = pygame_gui.UIManager(window_size)

# create a button and add it to the manager
button_size = (100, 50)
button_pos = (50, 50)
button_text = "Click me!"
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button_pos, button_size), text=button_text, manager=manager)

# main game loop
while True:
    # handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            # handle events for the GUI manager
            manager.process_events(event)

    # update the GUI manager
    manager.update(pygame.time.Clock().tick(60))

    # draw the GUI elements and update the Pygame display
    window.fill((255, 255, 255))
    manager.draw_ui(window)
    pygame.display.update()
