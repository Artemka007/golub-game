from typing import List
from src.core.controllers.coin import CoinController
from src.core.factories.coin import CoinFactory
from src.core.models.player import PlayerModel
from src.core.utils.binary_search import binary_search_left, binary_search_right
from src.core.utils.persistent_store import PersistentStore
from src.core.utils.subject import Subject


class CoinsState:
    def __init__(self, coins: List[CoinController], coins_collected: int):
        self.coins = coins
        self.coins_collected = coins_collected 


class CoinsStore(PersistentStore[CoinsState]):
    __coins = Subject[List[CoinController]]()
    __coins_collected = Subject[int]()

    coins = __coins.as_observable()
    coins_collected = __coins_collected.as_observable()

    def __init__(self, coins: List[CoinController]):
        super().__init__()

        self.__coins.next(coins)
        self.__coins_collected.next(0)

    def update_coins(self, coins: List[CoinController]):
        self.__coins.next(coins)

    def update_player(self, player: PlayerModel):
        coins = self.__coins.get_value()[:]
        coin_xs = [coin.model.rect.x for coin in coins]

        player_left = player.rect.left
        player_right = player.rect.right

        start = binary_search_left(coin_xs, player_left)
        end = binary_search_right(coin_xs, player_right)

        for i in range(start, end):
            coin = coins[i].model
            
            if coin.collected or not player.rect.colliderect(coin.rect):
                continue
            
            coin.collect()
            self.__coins_collected.next(self.__coins_collected.get_value() + 1)
            self.__coins.next(self.__coins.get_value())

    def save(self):
        coins = [CoinFactory.create_mvc_component(i.model.x, i.model.y, i.model.collected) for i in self.__coins.get_value()][:]
        coins_collected = self.__coins_collected.get_value()
        self._stack.push(CoinsState(coins, coins_collected))
    
    def undo(self):
        if self._stack.empty():
            return
        
        last_state = self._stack.pop()

        self.__coins.next(last_state.coins)
        self.__coins_collected.next(last_state.coins_collected)