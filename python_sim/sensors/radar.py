import pygame
import math

class Radar:
    def __init__(self, car):
        self.car = car
        self.distance = None
        self.valid = False

    def update(self, obstacles):
        self.distance = None
        self.valid = False
        radar_line = pygame.Rect(self.car.rect.centerx, self.car.rect.top - 200, 5, 200)

        for obs in obstacles:
            if radar_line.colliderect(obs):
                self.distance = (self.car.rect.top - obs.bottom) / 10.0
                self.valid = True
                break

    def draw(self, screen):
        if self.valid:
            pygame.draw.line(screen, (0, 255, 0), self.car.rect.midtop, (self.car.rect.centerx, self.car.rect.top - 200), 2)
