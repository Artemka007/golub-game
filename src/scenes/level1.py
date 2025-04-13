from src.core.coin import Coin
from src.core.platform import Platform
from src.scenes.scene import Scene


class Level1(Scene):
    def __init__(self):
        super().__init__()
        
        self._width = 4000
        self._height = 4000

        self.platforms.add(Platform(100, 300))
        self.platforms.add(Platform(400, 500))
        self.platforms.add(Platform(700, 200))
        self.platforms.add(Platform(1100, 600))

        self.coins.add(Coin(200 - 32, 230))
        self.coins.add(Coin(500 - 32, 530))
        self.coins.add(Coin(800 - 32, 230))