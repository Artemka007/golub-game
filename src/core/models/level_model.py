import pygame

from typing import List, Literal

from src.core.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.core.models.scene_model import Scene
from src.core.patterns.event_emitter import EventEmitter
from src.core.sprites.coin import Coin
from src.core.sprites.platform import Platform
from src.core.store.coins_store import CoinsStore
from src.core.camera import Camera
from src.core.sprites.player import Player
from src.core.store.level_store import LevelStore
from src.ui.coin_display import CoinDisplay
from src.ui.menu import Menu


class Level(Scene):
    def __init__(self, screen: pygame.Surface, platforms: List[Platform], coins: List[Coin]):
        super().__init__()
        
        self.screen = screen
        self.level_store = LevelStore()

        self.platforms = pygame.sprite.Group(platforms)
        self.coins = pygame.sprite.Group(coins)
        self.coins_collected = 0

        self.__load_background()
        
        self.player = Player()
        self.camera = Camera()

        self.__init_coins()
        self.__init_menu()
    
    def update(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.menu.visible:
                        self.menu.hide()
                    else:
                        self.menu.show()
                self.menu.handle_event(event)

            self.__draw_background()

            self.player.update(self)
            self.coins_store.update_player(self.player)

            self.camera.update(self.player, self)
            self.screen.blit(self.player.image, self.camera.apply(self.player))

            for platform in self.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            for coin in self.coins_store.coins:
                coin.update()
                coin.draw(self.screen, self.camera)
            
            self.coin_display.draw(self.screen)
            self.menu.draw()

    def __init_coins(self):
        self.coin_display = CoinDisplay()
        self.coins_store = CoinsStore(list(self.coins))
        self.coins_store.register_observer(self.coin_display)

    def __init_menu(self):
        self.emitter = EventEmitter[Literal['save', 'restart', 'cancel']]()
        self.emitter.on('save', lambda: self.game_store.save(self.player, self.coins_store.coins))
        self.emitter.on('restart', lambda: print('Restart'))
        self.emitter.on('cancel', lambda: print('Cancel!'))
        self.menu = Menu(self.screen, self.emitter)
    
    def __load_background(self):
        self.background = pygame.image.load("./assets/images/background.jpg").convert()

        original_width, original_height = self.background.get_size()
        self.background = pygame.transform.scale(self.background, (original_width * 2, original_height * 2))

    def __draw_background(self):
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        offset_x = int(self.camera.offset.x // 3) % bg_width
        offset_y = int(self.camera.offset.y // 3) % bg_height

        for x in range(-offset_x - bg_width, SCREEN_WIDTH + bg_width, bg_width):
            for y in range(-offset_y - bg_height, SCREEN_HEIGHT + bg_height, bg_height):
                self.screen.blit(self.background, (x, y))