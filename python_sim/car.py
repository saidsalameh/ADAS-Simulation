import pygame

class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 80)
        self.color = (0, 200, 255)

    def update(self):
        pass  # Static for now

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
