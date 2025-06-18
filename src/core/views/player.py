from typing import Union
import pygame
from src.core.models.player import PlayerModel


class PlayerView:
    def draw(self, surface: pygame.Surface, image: pygame.Surface, rect: pygame.Rect):
        surface.blit(image, rect)