from typing import Callable, Literal
import pygame
from src.core.utils.abstract_factory import AbstractMVCFactory
from src.core.utils.event_emitter import EventEmitter
from src.core.utils.observable import Observable
from src.ui.controllers.dead_menu import DeadMenuController
from src.ui.models.dead_menu import DeadMenuModel
from src.ui.views.dead_menu import DeadMenuView


class DeadMenuFactory(AbstractMVCFactory[DeadMenuModel, DeadMenuView, DeadMenuController]):
    def create_model(): 
        return DeadMenuModel()

    def create_view(screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        return DeadMenuView(screen, emitter)

    def create_controller(model, view):
        return DeadMenuController(model, view)
    
    def create_mvc_component(screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        model = DeadMenuFactory.create_model()
        view = DeadMenuFactory.create_view(screen, emitter)
        return DeadMenuFactory.create_controller(model, view)