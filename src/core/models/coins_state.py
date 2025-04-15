from typing import List

from src.core.sprites.coin import Coin


class CoinsState:
    def __init__(self, coins: List[Coin], coins_collected: int):
        self.coins = coins
        self.coins_collected = coins_collected 