import pygame
from sys import exit
from snake import *
from food import *
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True

# snake
snake = Snake((32, 32))  # Create a snake object

# food
food_list = []
food = Food((random.randint(0,512),random.randint(0,512)))
food_list.append(food)

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

    food.draw(screen)
    # RENDER YOUR GAME HERE
    snake.update(food, food_list)
    snake.draw(screen)
    

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(10)  #fps

