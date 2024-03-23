import pygame
from food import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill("white")
        self.direction = 'down'
        #position
        self.rect = self.image.get_rect(topleft = pos)
        #snake segment list
        self.snake_list = [pygame.Rect(self.rect)]
        

    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.direction != "left":
                self.direction = "right"
            elif event.key == pygame.K_LEFT and self.direction != "right":
                self.direction = "left"
            elif event.key == pygame.K_UP and self.direction != "down":
                self.direction = "up"
            elif event.key == pygame.K_DOWN and self.direction != "up":
                self.direction = "down"

    def col_check(self, food, food_list):
        if pygame.Rect.colliderect(self.rect, food.rect):
            print("hey")
            food_list.remove(food)
            

    def draw(self, screen):
        # Draw each segment of the snake
        for segment in self.snake_list:
            pygame.draw.rect(screen, (255, 255, 255), segment)

    def direction_check(self):
        if self.direction == "down":
            self.rect.y += 32
        elif self.direction == "up":
            self.rect.y -= 32
        if self.direction == "left":
            self.rect.x -= 32
        elif self.direction == "right":
            self.rect.x += 32

        if self.snake_list:
            for i in range(len(self.snake_list)-1, 0, -1):
                self.snake_list[i].x = self.snake_list[i-1].x
                self.snake_list[i].y = self.snake_list[i-1].y
            self.snake_list[0].x = self.rect.x
            self.snake_list[0].y = self.rect.y
      
    def update(self, food, food_list):
        self.direction_check()
        self.col_check(food, food_list)



        