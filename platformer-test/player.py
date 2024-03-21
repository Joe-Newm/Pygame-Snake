import pygame
from pygame.sprite import Group
from tiles import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        #self.speed = 7
        self.gravity = 0.8
        self.jump_speed = -16
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed = 0
        self.touch_ground = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.speed = 7
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.speed = -7
        else:
            self.direction.x = 0
            self.speed = self.speed * 0.8
        if keys[pygame.K_SPACE]:
            if self.touch_ground == True:
                self.jump()
                



    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

        

    def jump(self):
        self.direction.y = self.jump_speed

    def touch_ground_check(self):
        # check if player is touching the ground

        if self.direction.y == 0.0:
            self.touch_ground = True
        else:
            self.touch_ground = False 
        

    def update(self):
        self.get_input()
        self.touch_ground_check()


# projectiles class

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft = pos)


    def shoot():
        bullet = Bullet((Player.rect.x))


        
       

