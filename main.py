import pygame
from sys import exit
from snake import *
from food import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((512, 512))
clock = pygame.time.Clock()
running = True

# snake

snake = Snake((32, 32))  # Create a snake object


# food

food = Food((128,128))



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
    food.draw(screen)
    snake.update(food)
    snake.draw(screen)
    

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(10)  # limits FPS to 60

