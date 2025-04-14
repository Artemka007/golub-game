import pygame

from src.core.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.core.sprites.player import Player
from src.scenes.scene import Scene


class Camera:
    @property
    def offset(self):
        return pygame.Vector2(self.camera.x, self.camera.y)
    
    def __init__(self):
        self.camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def apply(self, target: pygame.sprite.Sprite):
        return target.rect.move(-self.camera.x, -self.camera.y)

    def update(self, player: Player, scene: Scene):
        self.camera.x = player.rect.centerx - SCREEN_WIDTH // 2
        self.camera.y = player.rect.centery - SCREEN_HEIGHT // 2

        self.camera.x = max(0, min(self.camera.x, scene.width - SCREEN_WIDTH))
        self.camera.y = max(0, min(self.camera.y, scene.height - SCREEN_HEIGHT))