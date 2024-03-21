import pygame
from sys import exit
from settings import *
from tiles import Tile
from level import Level
from player import Player

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

test_tile = pygame.sprite.Group(Tile((100,100), 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    screen.fill("black")

    level.run()

    pygame.display.update()
    clock.tick(60)