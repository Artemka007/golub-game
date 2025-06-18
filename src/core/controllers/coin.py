import pygame
from src.core.camera import Camera
from src.core.models.coin import CoinModel
from src.core.views.coin import CoinView


class CoinController(pygame.sprite.Sprite):
    def __init__(self, model: CoinModel, view: CoinView):
        super().__init__()
        self.model = model
        self.view = view

    def update(self):
        self.model.update()

    def draw(self, screen: pygame.Surface, camera: Camera):
        self.view.draw(screen, self.model, camera, self.model.image)

    def collect(self):
        if self.model.collected:
            return
        
        self.model.collect()

    def recollect(self):
        self.model.recollect()