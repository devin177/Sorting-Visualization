"""Button Class that will be used to iterate through algorithms
or change options"""
import pygame

class Button:
    """Definition of Button Class"""

    def __init__(self, window, color, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.window = window
        self.color = color

    def draw(self):
        """Draw method"""
        #pygame.draw.rect(self.window, (0, 0, 0), [self.x, self.y, self.width, self.height])
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height])
        font = pygame.font.SysFont("impact", 30)
        text = font.render(self.text, 1, (0, 0, 0))
        self.window.blit(text, ((self.x + self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def above(self, position):
        """Checks to see if my mouse is over the button"""
        if(position[0] >= self.x and position[0] < self.x + self.width):
            if(position[1] < self.y and position[1] > self.y + self.height):
                return True
