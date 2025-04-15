import pygame
from src.core.models.level_model import Level
from src.core.sprites.coin import Coin
from src.core.sprites.platform import Platform


platforms = [
    Platform(100, 300),
    Platform(400, 500),
    Platform(700, 200),
    Platform(1100, 600)
]


coins = [
    Coin(200 - 32, 230),
    Coin(500 - 32, 430),
    Coin(800 - 32, 130)
]

class Level1(Level):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen, platforms, coins)

        self._width = 4000
        self._height = 4000