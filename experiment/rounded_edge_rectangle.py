import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def rounded_rect(screen,rect,color=(255,255,255)):
    rect_x,rect_y,rect_width,rect_height = rect
    print(rect_x,rect_y,rect_width,rect_height)
    corner_radius = rect_height//2
    pygame.draw.rect(screen, color, (rect_x + corner_radius, rect_y, rect_width - 2*corner_radius, rect_height))
    pygame.draw.rect(screen, color, (rect_x, rect_y + corner_radius, rect_width, rect_height - 2*corner_radius))

    # Draw circles to create rounded edges
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + corner_radius, rect_y + rect_height - corner_radius), corner_radius)
    pygame.draw.circle(screen, color, (rect_x + rect_width - corner_radius, rect_y + rect_height - corner_radius), corner_radius)



                 
# Update the screen
pygame.display.update()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    rounded_rect(screen,(100,100,200,20),(255,255,0))
    pygame.display.update()
