from typing import List
from src.core.sprites.player import Player
from src.core.sprites.coin import Coin
from src.core.patterns.observer import Subject


class CoinsStore(Subject):
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, coins: List[Coin]):
        self.__coins = coins

    @property
    def coins_collected(self):
        return self.__coins_collected

    def __init__(self, coins: List[Coin]):
        super().__init__()
        self.__coins = coins
        self.__coins_collected = 0

    def update_player(self, player: Player):
        for coin in self.__coins[:]:
            if coin.collected or not player.rect.colliderect(coin.rect):
                continue
            coin.collect()
            self.__coins_collected += 1
            self.notify_observers(self.coins_collected)
            self.__coins.remove(coin)