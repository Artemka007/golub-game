import pygame
from src.core.store.coins_store import CoinsStore
from src.core.models.game_state_model import GameState
from src.core.patterns.observer import Observer
from src.core.patterns.stack import Stack
from src.core.sprites.coin import Coin
from src.core.sprites.player import Player


class PersistentLevelStore:
    def __init__(self):
        self.stack = Stack[GameState]()
    
    def save(self, player: Player, coins: pygame.sprite.Group):
        self.stack.push(
            GameState(pygame.Vector2(player.rect.x, player.rect.y), [i for i in coins][:])
        )
    
    def apply(self, player: Player, coin_manager: CoinsStore):
        if self.stack.empty():
            return
        last_state = self.stack.pop()
        player.move(last_state.player_position)
        print(last_state.coins.__len__())
        coin_manager.coins = last_state.coins
        coin_manager.coins_collected = len([i for i in last_state.coins if i.collected])
        