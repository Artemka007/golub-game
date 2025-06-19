from typing import Callable
import pygame
from src.core.utils.abstract_factory import AbstractMVCFactory
from src.core.utils.observable import Observable
from src.ui.controllers.coin_display import CoinDisplayController
from src.ui.models.coin_display import CoinDisplayModel
from src.ui.views.coin_display import CoinDisplayView


class CoinDisplayFactory(AbstractMVCFactory[CoinDisplayModel, CoinDisplayView, CoinDisplayController]):
    def create_model(): 
        return CoinDisplayModel()

    def create_view(screen: pygame.Surface):
        return CoinDisplayView(screen)

    def create_controller(model, view, coins_collected: Observable[int]):
        return CoinDisplayController(model, view, coins_collected)
    
    def create_mvc_component(screen: pygame.Surface, coins_collected: Observable[int]):
        model = CoinDisplayFactory.create_model()
        view = CoinDisplayFactory.create_view(screen)
        return CoinDisplayFactory.create_controller(model, view, coins_collected)