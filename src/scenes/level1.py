from src.core.platform import Platform
from src.scenes.scene import Scene


class Level1(Scene):
    def __init__(self):
        super().__init__()
        
        self._width = 4000
        self._height = 4000

        self.platforms.add(Platform(100, 300))
        self.platforms.add(Platform(400, 500))
