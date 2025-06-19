from typing import Literal

import pygame
from src.core.controllers.player import PlayerController
from src.core.models.player import PlayerModel
from src.core.utils.event_emitter import EventEmitter
from src.core.views.player import PlayerView
from src.core.utils.abstract_factory import AbstractMVCFactory


class PlayerFactory(AbstractMVCFactory[PlayerModel, PlayerView, PlayerController]):
    def create_model(emitter: EventEmitter[Literal['player_dead']]):
        return PlayerModel(emitter)

    def create_view():
        return PlayerView()

    def create_controller(model, view):
        return PlayerController(model, view)
    
    def create_mvc_component(emitter: EventEmitter[Literal['player_dead']]):
        model = PlayerFactory.create_model(emitter)
        view = PlayerFactory.create_view()
        return PlayerFactory.create_controller(model, view)