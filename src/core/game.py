import sys
from typing import Literal
import pygame

from src.core.patterns.event_emitter import EventEmitter
from src.core.store.coins_store import CoinsStore
from src.core.camera import Camera
from src.core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.core.sprites.player import Player
from src.core.store.level_store import LevelStore
from src.scenes.level1 import Level1
from src.ui.coin_display import CoinDisplay
from src.ui.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Голубь в космосе")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.current_scene = Level1(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_scene.update()

            pygame.display.flip()
            self.clock.tick(FPS)