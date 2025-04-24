import pygame
import random

class World:
    def __init__(self):
        self.obstacles = []

    def update(self):
        if random.randint(0, 30) == 0:
            lane = random.choice([150, 375, 600])
            self.obstacles.append(pygame.Rect(lane, -100, 50, 80))

        for obs in self.obstacles:
            obs.y += 5

        self.obstacles = [obs for obs in self.obstacles if obs.y < 600]

    def draw(self, screen):
        for lane_x in [150, 375, 600]:
            pygame.draw.line(screen, (200, 200, 200), (lane_x, 0), (lane_x, 600), 2)

        for obs in self.obstacles:
            pygame.draw.rect(screen, (255, 0, 0), obs)
