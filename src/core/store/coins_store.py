from typing import List
from src.core.models.coins_state import CoinsState
from src.core.patterns.persistent_store import PersistentStore
from src.core.patterns.stack import Stack
from src.core.sprites.player import Player
from src.core.sprites.coin import Coin
from src.core.patterns.observer import Subject


class CoinsStore(PersistentStore[CoinsState], Subject):
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, coins: List[Coin]):
        self.__coins = coins

    @property
    def coins_collected(self):
        return self.__coins_collected
    
    @coins_collected.setter
    def coins_collected(self, coins_collected: int):
        self.__coins_collected = coins_collected

    def __init__(self, coins: List[Coin]):
        super().__init__()
        self.__coins = coins
        self.__coins_collected = 0
        self._stack = Stack[CoinsState]()

    def update_player(self, player: Player):
        for coin in self.__coins[:]:
            if coin.collected or not player.rect.colliderect(coin.rect):
                continue
            coin.collect()
            self.__coins_collected += 1
            self.notify_observers(self.coins_collected)
            self.__coins.remove(coin)

    def save(self):
        self._stack.push(
            CoinsState([Coin(i.x, i.y) for i in self.coins][:], self.coins_collected)
        )
    
    def undo(self):
        if self._stack.empty():
            return
        
        last_state = self._stack.pop()

        self.coins = last_state.coins
        self.coins_collected = last_state.coins_collected
        self.notify_observers(last_state.coins_collected)