from typing import List
from src.core.sprites.player import Player
from src.core.sprites.coin import Coin
from src.core.observer import Subject


class CoinManager(Subject):
    def __init__(self, coins: List[Coin]):
        super().__init__()
        self.coins = coins
        self.coins_collected = 0

    def update_player(self, player: Player):
        for coin in self.coins[:]:
            if not coin.collected and player.rect.colliderect(coin.rect):
                coin.collect()
                self.coins_collected += 1
                self.notify_observers(self.coins_collected)
                self.coins.remove(coin)