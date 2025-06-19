from src.core.controllers.coin import CoinController
from src.core.models.coin import CoinModel
from src.core.views.coin import CoinView
from src.core.utils.abstract_factory import AbstractMVCFactory


class CoinFactory(AbstractMVCFactory[CoinModel, CoinView, CoinController]):
    def create_model(x: int, y: int, collected: bool = False):
        return CoinModel(x, y, collected)

    def create_view():
        return CoinView()

    def create_controller(model, view):
        return CoinController(model, view)
    
    def create_mvc_component(x: int, y: int, collected: bool = False):
        model = CoinFactory.create_model(x, y, collected)
        view = CoinFactory.create_view()
        return CoinFactory.create_controller(model, view)