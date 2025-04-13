import math
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, animation_speed=5):
        super().__init__()
        
        self.image = pygame.image.load('./assets/images/money.png')
        self.original_width, self.original_height = self.image.get_size()

        self.x = x
        self.y = y
        self.animation_speed = animation_speed
        self.angle = 0 

        self.rect = self.image.get_rect(topleft=(x, y))

        self.collected = False

    def update(self):
        self.angle += self.animation_speed
        if self.angle >= 360:
            self.angle = 0

    def draw(self, screen):
        if not self.collected:
            scale = abs(math.cos(self.angle * (3.14 / 180)))
            new_width = int(self.original_width * scale)
            scaled_image = pygame.transform.scale(self.image, (new_width, self.original_height))
            x_offset = (self.original_width - new_width) // 2
            screen.blit(scaled_image, (self.x + x_offset, self.y))

    def collect(self):
        self.collected = True
