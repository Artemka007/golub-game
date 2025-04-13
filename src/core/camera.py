import pygame

from src.core.constants import *
from src.core.player import Player
from src.scenes.scene import Scene


class Camera:
    def __init__(self):
        self.camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def apply(self, player: Player):
        # Смещение объекта относительно камеры
        return player.rect.move(-self.camera.x, -self.camera.y)

    def update(self, player: Player, scene: Scene):
        # Центрируем камеру на игроке
        self.camera.x = player.rect.centerx - SCREEN_WIDTH // 2
        self.camera.y = player.rect.centery - SCREEN_HEIGHT // 2

        # Ограничиваем камеру границами уровня
        self.camera.x = max(0, min(self.camera.x, scene.width - SCREEN_WIDTH))
        self.camera.y = max(0, min(self.camera.y, scene.height - SCREEN_HEIGHT))