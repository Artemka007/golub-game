import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=200, height=50):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))  # Белый цвет платформы
        self.rect = self.image.get_rect(topleft=(x, y))
