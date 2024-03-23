import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

    def col_check(self, snake, food_list):
        if pygame.Rect.colliderect(self.rect, snake.rect):
            print("hey")
            snake.snake_list.append(pygame.Rect(snake.rect))
            food_list.empty()
            food = Food((random.randint(0,15)*32,random.randint(0,15)*32))
            food_list.add(food)
            

    def update(self, snake, food_list):
        self.col_check(snake, food_list)
