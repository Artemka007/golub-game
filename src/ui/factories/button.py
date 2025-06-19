from typing import Callable
import pygame

from src.core.utils.abstract_factory import AbstractMVCFactory
from src.ui.controllers.button import ButtonController
from src.ui.models.button import ButtonModel
from src.ui.views.button import ButtonView


class ButtonFactory(AbstractMVCFactory[ButtonModel, ButtonView, ButtonController]):
    def create_model(rect: pygame.Rect, text: str, font: pygame.font.Font): 
        return ButtonModel(rect, text, font)

    def create_view(screen: pygame.Surface, callback: Callable):
        return ButtonView(screen, callback)

    def create_controller(model, view):
        return ButtonController(model, view)
    
    def create_mvc_component(screen: pygame.Surface, rect: pygame.Rect, text: str, font: pygame.font.Font, callback: Callable):
        model = ButtonFactory.create_model(rect, text, font)
        view = ButtonFactory.create_view(screen, callback)
        return ButtonFactory.create_controller(model, view)