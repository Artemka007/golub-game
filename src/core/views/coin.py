import math
import pygame

from src.core.camera import Camera
from src.core.models.coin import CoinModel


class CoinView:
    def draw(self, screen: pygame.Surface, model: CoinModel, camera: Camera, image: pygame.Surface):
        if model.collected:
            return
        
        original_width, original_height = image.get_size()
        scale = abs(math.cos(model.angle * (3.14 / 180)))
        new_width = int(original_width * scale)
        scaled_image = pygame.transform.scale(image, (new_width, original_height))
        x_offset = (original_width - new_width) // 2
        self.rect = pygame.Rect(model.x, model.y, original_width, original_height)
        screen.blit(scaled_image, (camera.apply(self).x + x_offset, camera.apply(self).y))