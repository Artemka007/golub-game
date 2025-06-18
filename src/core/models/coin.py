import pygame


class CoinModel:
    def __init__(self, x: int, y: int, collected: bool = False):
        self.image = pygame.image.load('./assets/images/money.png')
        self.x = x
        self.y = y
        self.animation_speed = 5
        self.angle = 0
        self.collected = collected
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.angle += self.animation_speed
        if self.angle >= 360:
            self.angle = 0

    def collect(self):
        self.collected = True

    def recollect(self):
        self.collected = False