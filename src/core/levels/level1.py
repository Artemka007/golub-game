import pygame
from src.core.controllers.level import LevelController
from src.core.factories.coin import CoinFactory
from src.core.factories.level import LevelFactory
from src.core.factories.platform import PlatformFactory


class Level1:
    platforms = [PlatformFactory.create_mvc_component(*i) for i in [
        (100, 300), 
        (400, 500),
        (700, 200),
        (1100, 600)
    ]]


    coins = [CoinFactory.create_mvc_component(*i) for i in [
        (200 - 32, 230),
        (500 - 32, 430),
        (800 - 32, 130)
    ]]


    def __new__(cls, surface: pygame.Surface) -> LevelController:
        return LevelFactory.create_mvc_component(surface, 1000, 2000).build(cls.platforms, cls.coins)