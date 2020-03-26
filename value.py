"""Definition of bubble class which will be used
to contain the data of the lists"""
import pygame

class Value:
    """Definition of bubble class"""
    def __init__(self, value):
        self.value = value

    def draw(self, display, left_corner, width):
        """"Draw function for the bubbles"""
        pygame.draw.rect(display, (0, 0, 255), [left_corner, 600, width, -20*self.value])
        font = pygame.font.SysFont("impact", 30)
        text = font.render(str(self.value), 1, (0, 0, 0))
        display.blit(text, ((left_corner + width/2 - text.get_width()/2), 500 + (50 - text.get_height()/2)))
