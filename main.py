import pygame
from sys import exit
from snake import *
from food import *
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Joe Newm's Snake Game")
clock = pygame.time.Clock()
running = True

# snake
snake_group = pygame.sprite.Group()
snake = Snake((32, 32))  # Create a snake object
snake_group.add(snake)


# food
food_list = pygame.sprite.Group()
food = Food((random.randint(0,15)*32,random.randint(0,15)*32))
food_list.add(food)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        snake.get_input(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    snake_group.update(screen)
    snake_group.draw(screen)
    
    food_list.update(snake, food_list)
    food_list.draw(screen)
    
    

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(10)  #fps

