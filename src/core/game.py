import sys
from typing import Literal
import pygame

from src.core.patterns.event_emitter import EventEmitter
from src.core.store.coins_store import CoinsStore
from src.core.camera import Camera
from src.core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.core.sprites.player import Player
from src.core.store.game_store import GameStore
from src.scenes.level1 import Level1
from src.ui.coin_display import CoinDisplay
from src.ui.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Голубь в космосе")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load("./assets/images/background.jpg").convert()

        original_width, original_height = self.background.get_size()
        self.background = pygame.transform.scale(self.background, (original_width * 2, original_height * 2))

        self.clock = pygame.time.Clock()
        self.player = Player()
        self.camera = Camera()
        self.current_scene = Level1()
        self.coins_collected = 0

        self.coin_display = CoinDisplay()
        self.coins_store = CoinsStore(list(self.current_scene.coins))
        self.coins_store.register_observer(self.coin_display)

        self.game_store = GameStore()

        self.emitter = EventEmitter[Literal['save', 'restart', 'cancel']]()
        self.emitter.on('save', lambda: self.game_store.save(self.player, self.coins_store.coins))
        self.emitter.on('restart', lambda: print('Restart'))
        self.emitter.on('cancel', lambda: print('Cancel!'))
        self.menu = Menu(self.screen, self.emitter)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.menu.visible:
                        self.menu.hide()
                    else:
                        self.menu.show()
                self.menu.handle_event(event)

            self.__render_background()

            self.player.update(self.current_scene)
            self.coins_store.update_player(self.player)

            self.camera.update(self.player, self.current_scene)
            self.screen.blit(self.player.image, self.camera.apply(self.player))

            for platform in self.current_scene.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            for coin in self.coins_store.coins:
                coin.update()
                coin.draw(self.screen, self.camera)
            
            self.coin_display.draw(self.screen)
            self.menu.draw()

            pygame.display.flip()
            self.clock.tick(FPS)
    
    def __render_background(self):
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        offset_x = int(self.camera.offset.x // 3) % bg_width
        offset_y = int(self.camera.offset.y // 3) % bg_height

        for x in range(-offset_x - bg_width, SCREEN_WIDTH + bg_width, bg_width):
            for y in range(-offset_y - bg_height, SCREEN_HEIGHT + bg_height, bg_height):
                self.screen.blit(self.background, (x, y))