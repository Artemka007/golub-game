import sys
import pygame

from src.core.camera import Camera
from src.core.constants import *
from src.core.player import Player
from src.scenes.level1 import Level1


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Прыжки по платформам")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.camera = Camera()
        self.all_sprites.add(self.player)
        self.current_scene = Level1()  # Начальная сцена

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Обновление логики игрока
            self.player.update(self.current_scene)

            # Очистка экрана
            self.screen.fill((0, 0, 0))

            # Отрисовка сцены и игрока
            self.camera.update(self.player, self.current_scene)
            self.screen.blit(self.player.image, self.camera.apply(self.player))

            for platform in self.current_scene.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            pygame.display.flip()
            self.clock.tick(FPS)