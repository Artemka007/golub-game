from src.core.utils.observable import Observable
from src.ui.models.coin_display import CoinDisplayModel
from src.ui.views.coin_display import CoinDisplayView


class CoinDisplayController:
    def __init__(self, model: CoinDisplayModel, view: CoinDisplayView, coins_collected: Observable[int]):
        self.model = model
        self.view = view
        self.coins_collected = 0
        coins_collected.subscribe(self.update)

    def update(self, coins_collected):
        self.coins_collected = coins_collected

    def draw(self):
        self.view.draw(self.model.coin_image, self.coins_collected)