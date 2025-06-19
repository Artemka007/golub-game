from typing import Callable, Literal
import pygame
from src.core.utils.abstract_factory import AbstractMVCFactory
from src.core.utils.event_emitter import EventEmitter
from src.ui.controllers.menu import MenuController
from src.ui.models.menu import MenuModel
from src.ui.views.menu import MenuView


class MenuFactory(AbstractMVCFactory[MenuModel, MenuView, MenuController]):
    def create_model(): 
        return MenuModel()

    def create_view(screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        return MenuView(screen, emitter)

    def create_controller(model, view):
        return MenuController(model, view)
    
    def create_mvc_component(screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        model = MenuFactory.create_model()
        view = MenuFactory.create_view(screen, emitter)
        return MenuFactory.create_controller(model, view)