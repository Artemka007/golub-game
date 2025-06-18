from typing import Literal
import pygame
from src.core.controllers.level import LevelController
from src.core.models.level import LevelModel
from src.core.utils.event_emitter import EventEmitter
from src.core.utils.abstract_factory import AbstractMVCFactory
from src.core.views.level import LevelView


class LevelFactory(AbstractMVCFactory[LevelModel, LevelView, LevelController]):
    def create_model(emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']], width: int, height: int):
        return LevelModel(emitter, width, height)

    def create_view(model: LevelModel, surface: pygame.Surface, emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']]):
        return LevelView(model, surface, emitter)

    def create_controller(model, view, emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']]):
        return LevelController(model, view, emitter)
    
    def create_mvc_component(surface: pygame.Surface, width: int, height: int) -> LevelController:
        emitter = EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']]()
        model = LevelFactory.create_model(emitter, width, height)
        view = LevelFactory.create_view(model, surface, emitter)
        controller = LevelFactory.create_controller(model, view, emitter)
        return controller