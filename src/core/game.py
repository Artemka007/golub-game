import sys
import pygame

from src.core.coin_manager import CoinManager
from src.core.observable import Observer
from src.core.camera import Camera
from src.core.constants import *
from src.core.player import Player
from src.scenes.level1 import Level1


class Game(Observer):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load("./assets/images/background.jpg").convert()
        pygame.display.set_caption("Прыжки по платформам")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.camera = Camera()
        self.all_sprites.add(self.player)
        self.current_scene = Level1()
        self.coins_collected = 0
        self.coin_manager = CoinManager(self.current_scene.coins)
        self.coin_manager.register_observer(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.update(self.current_scene)
            self.coin_manager.update_player(self.player)

            self.screen.fill((0, 0, 0))

            self.camera.update(self.player, self.current_scene)
            self.screen.blit(self.player.image, self.camera.apply(self.player))

            for platform in self.current_scene.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            for coin in filter(lambda x: not x.collected, self.current_scene.coins):
                coin.update()
                coin.draw(self.screen)
                self.screen.blit(coin.image, self.camera.apply(coin))

            pygame.display.flip()
            self.clock.tick(FPS)

    def update(self, coins_collected):
        self.coins_collected = coins_collected