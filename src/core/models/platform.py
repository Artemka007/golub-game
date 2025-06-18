import pygame


class PlatformModel:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.image = pygame.image.load('./assets/images/platform.png')
        
        original_width, original_height = self.image.get_size()
        
        self.width = original_width // 5
        self.height = original_height // 5
        
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        crop_rect = pygame.Rect(0, 50, self.image.get_width(), self.image.get_height() // 2)
        self.image = self.image.subsurface(crop_rect)
        self.rect = self.image.get_rect(topleft=(x, y))