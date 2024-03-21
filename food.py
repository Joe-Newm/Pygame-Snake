import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill('blue')

        #position
        self.rect = self.image.get_rect(topleft = pos)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)