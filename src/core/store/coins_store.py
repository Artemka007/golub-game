from typing import List
from src.core.models.coins_state import CoinsState
from src.core.patterns.binary_search import binary_search_left, binary_search_right
from src.core.patterns.persistent_store import PersistentStore
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

    def update_coins(self, coins: List[Coin]):
        self.__coins.next(coins)

    def update_player(self, player: Player):
        coins = self.__coins.get_value()[:]
        coin_xs = [coin.rect.x for coin in coins]

        player_left = player.rect.left
        player_right = player.rect.right

        start = binary_search_left(coin_xs, player_left)
        end = binary_search_right(coin_xs, player_right)

        for i in range(start, end):
            coin = coins[i]
            if coin.collected or not player.rect.colliderect(coin.rect):
                continue
            coin.collect()
            self.__coins_collected.next(self.__coins_collected.get_value() + 1)
            self.__coins.next(self.__coins.get_value())

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