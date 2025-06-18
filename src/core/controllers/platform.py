import pygame
from src.core.camera import Camera
from src.core.models.platform import PlatformModel
from src.core.views.platform import PlatformView


class PlatformController(pygame.sprite.Sprite):
    def __init__(self, model: PlatformModel, view: PlatformView):
        super().__init__()
        self.model = model
        self.view = view
  
    def draw(self, screen: pygame.Surface, camera: Camera):
        self.view.draw(screen, self.model, camera, self.model.image)
