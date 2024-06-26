import pygame
from sys import exit
from snake import *
from food import *
import random

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((512, 512))
    pygame.display.set_caption("Joe Newm's Snake Game")
    clock = pygame.time.Clock()
    running = True

    # snake
    snake_group = pygame.sprite.Group()
    snake = Snake((32, 32))  # Create a snake object
    snake_group.add(snake)
    snake.rect.x = 32
    snake.rect.y = 32

    # food
    food_list = pygame.sprite.Group()
    food = Food((random.randint(0,15)*32,random.randint(0,15)*32))
    food_list.add(food)

    return screen, clock, running, snake_group, snake, food_list, food

running = True
#controller
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

screen, clock, running, snake_group, snake, food_list, food = init_game()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        snake.get_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit
                exit()
            if event.key == pygame.K_r:
                init_game()
                print("hey")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    ## snake render
    snake_group.update(screen)
    snake_group.draw(screen)
    ## food render
    food_list.update(snake, food_list)
    food_list.draw(screen)
    
    

    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(10)  #fps

