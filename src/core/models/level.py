from typing import List, Literal

import pygame
from src.core.controllers.coin import CoinController
from src.core.controllers.platform import PlatformController
from src.core.controllers.player import PlayerController
from src.core.camera import Camera
from src.core.factories.player import PlayerFactory
from src.core.utils.scene_model import Scene
from src.core.utils.event_emitter import EventEmitter
from src.core.store.coins_store import CoinsStore
from src.core.store.player_store import PlayerStore


class LevelModel(Scene):
    def __init__(self, emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']], width: int, height: int):
        self.player: PlayerController = PlayerFactory.create_mvc_component(emitter)
        self.camera = Camera()

        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.player_store = PlayerStore(self.player)
        self.coins_store = CoinsStore([])

        self.coins_collected = 0

        self._width = width
        self._height = height

        self.emitter = emitter

        self.coins_store.coins.unsubscribe(self.update_coins)
        self.coins_store.coins.subscribe(self.update_coins)
    
    def update_coins(self, coins):
        self.coins = pygame.sprite.Group(coins)

    def build(self, platforms: List[PlatformController], coins: List[CoinController]):
        self.platforms = pygame.sprite.Group(platforms)
        self.coins = pygame.sprite.Group(coins)
        self.coins_store.update_coins(coins)

    def update(self):
        self.player.update(self)
        self.coins_store.update_player(self.player.model)
        self.camera.update(self.player.model, self)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            self.player_store.undo()
            self.coins_store.undo()
    
    def reset(self):
        platforms = list(self.platforms)
        coins = list(self.coins)
        for i in coins:
            i.recollect()
        self.__init__(self.emitter, self._width, self._height)
        self.build(platforms, coins)