import pygame
from car import Car
from world import World
from sensors.radar import Radar
from state_output import export_radar_data

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

car = Car(375, 500)
world = World()
radar = Radar(car)

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.update()
    car.update()
    radar.update(world.obstacles)

    world.draw(screen)
    car.draw(screen)
    radar.draw(screen)

    export_radar_data(radar)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
