from typing import List
from src.core.models.coins_state import CoinsState
from src.core.patterns.persistent_store import PersistentStore
from src.core.patterns.stack import Stack
from src.core.patterns.subject import Subject
from src.core.sprites.player import Player
from src.core.sprites.coin import Coin


class CoinsStore(PersistentStore[CoinsState]):
    __coins = Subject[List[Coin]]()
    __coins_collected = Subject[int]()

    coins = __coins.as_observable()
    coins_collected = __coins_collected.as_observable()

    def __init__(self, coins: List[Coin]):
        super().__init__()

        self.__coins.next(coins)
        self.__coins_collected.next(0)

        self._stack = Stack[CoinsState]()

    def update_player(self, player: Player):
        for coin in self.__coins.get_value()[:]:
            if coin.collected or not player.rect.colliderect(coin.rect):
                continue
            coin.collect()
            self.__coins_collected.next(self.__coins_collected.get_value() + 1)
            self.__coins.next(list(filter(lambda x: x != coin, self.__coins.get_value())))

    def save(self):
        self._stack.push(
            CoinsState([Coin(i.x, i.y) for i in self.__coins.get_value()][:], self.__coins_collected.get_value())
        )
    
    def undo(self):
        if self._stack.empty():
            return
        
        last_state = self._stack.pop()

        self.__coins.next(last_state.coins)
        self.__coins_collected.next(last_state.coins_collected)