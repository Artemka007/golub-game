from typing import List, Literal

import pygame

from src.core.controllers.coin import CoinController
from src.core.controllers.platform import PlatformController
from src.core.models.level import LevelModel
from src.core.utils.event_emitter import EventEmitter
from src.core.views.level import LevelView


class LevelController(pygame.sprite.Sprite):
    def __init__(self, model: LevelModel, view: LevelView, emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']]):
        super().__init__()
        self.model = model
        self.view = view
        self.emitter = emitter
        self.emitter.on('save', self.__save_state)
        self.emitter.on('restart', self.__restart_game)
        self.emitter.on('cancel', self.__cancel)
        self.emitter.on('player_dead', self.__player_dead)

    def build(self, platforms: List[PlatformController], coins: List[CoinController]):
        self.model.build(platforms, coins)
        return self

    def update(self):
        self.model.update()
        self.view.draw(self.model)

    def handle_event(self, event: pygame.event.Event):
        self.model.handle_event(event)
        self.view.handle_event(event)

    def __save_state(self):
        self.model.player_store.save()
        self.model.coins_store.save()
        self.view.menu.model.hide()

    def __restart_game(self): 
        self.model.reset()
        self.view.reset(self.model)
        self.emitter.off('save', self.__save_state)
        self.emitter.off('restart', self.__restart_game)
        self.emitter.off('cancel', self.__cancel)
        self.emitter.off('player_dead', self.__player_dead)
        self.__init__(self.model, self.view, self.emitter)

    def __player_dead(self): 
        self.view.dead_menu.model.show()
        self.emitter.off('player_dead', self.__player_dead)
    
    def __cancel(self): 
        self.view.menu.model.hide()