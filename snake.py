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
        self.snake_list = []
        self.direction_change_allowed = True
        self.vel = 0


        

    def get_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.image.fill("white")
            if self.direction_change_allowed:
                if event.key == pygame.K_RIGHT and self.direction != "left":
                    self.direction = "right"
                elif event.key == pygame.K_LEFT and self.direction != "right":
                    self.direction = "left"
                elif event.key == pygame.K_UP and self.direction != "down":
                    self.direction = "up"
                elif event.key == pygame.K_DOWN and self.direction != "up":
                    self.direction = "down"
            self.direction_change_allowed = False

        if event.type == pygame.JOYBUTTONDOWN:
            self.image.fill("white")
            if self.direction_change_allowed:
                if event.button == 14 and self.direction != "left":
                    self.direction = "right"
                elif event.button == 13 and self.direction != "right":
                    self.direction = "left"
                elif event.button == 11 and self.direction != "down":
                    self.direction = "up"
                elif event.button == 12 and self.direction != "up":
                    self.direction = "down"
            self.direction_change_allowed = False

        



    def direction_check(self):
        self.vel = 32
        if self.direction == "down":
            self.rect.y += self.vel
        elif self.direction == "up":
            self.rect.y -= self.vel
        if self.direction == "left":
            self.rect.x -= self.vel
        elif self.direction == "right":
            self.rect.x += self.vel
        if self.direction == "stop":
            self.vel = 0

    def death(self):
        self.direction = "stop"
        self.image.fill("red")

    def death_check(self):
        if self.rect.x < 0:
            self.death()
            self.rect.x += 32
        if self.rect.x > 480:
            self.death()
            self.rect.x -= 32
        if self.rect.y < 0:
            self.death()
            self.rect.y += 32
        if self.rect.y > 480:
            self.death()
            self.rect.y -= 32

            
      
    def update(self, screen):
        self.direction_check()
        self.direction_change_allowed = True
        self.death_check()

        for segment in self.snake_list:
            pygame.draw.rect(screen, (255, 255, 255), segment)

        if self.snake_list:
            for i in range(len(self.snake_list)-1, 0, -1):
                self.snake_list[i].x = self.snake_list[i-1].x
                self.snake_list[i].y = self.snake_list[i-1].y
            self.snake_list[0].x = self.rect.x
            self.snake_list[0].y = self.rect.y
        



        