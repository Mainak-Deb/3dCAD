import pygame

def display_text(surface, text, font, color, position):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center=position
    surface.blit(text_obj, text_rect)
       
def modify_color(color,value):
        return (min(int(color[0]*value/100),255),min(int(color[1]*value/100),255),min(int(color[2]*value/100),255))

def hoverable_circle(window_surface, circle_color, circle_position, circle_radius):
        mouse_pos = pygame.mouse.get_pos()
        if ((mouse_pos[0] - circle_position[0]) ** 2 + (mouse_pos[1] - circle_position[1]) ** 2) <= circle_radius ** 2:
            color = modify_color(circle_color,85) 
        else:
           color =circle_color
        pygame.draw.circle(window_surface, color, circle_position, circle_radius)
        
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
