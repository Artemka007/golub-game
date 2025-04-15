import pygame
from src.core.store.coins_store import CoinsStore
from src.core.models.game_state_model import GameState
from src.core.patterns.observer import Observer
from src.core.patterns.stack import Stack
from src.core.sprites.coin import Coin
from src.core.sprites.player import Player


class LevelStore:
    def __init__(self):
        self.stack = Stack[GameState]()
    
    def save(self, player: Player, coins: pygame.sprite.Group):
        self.stack.push(
            GameState(pygame.Vector2(player.rect.x, player.rect.y), coins)
        )
    
    def apply(self, player: Player, coin_manager: CoinsStore):
        last_state = self.stack.pop()
        player.move(last_state.player_position)
        coin_manager.coins = last_state.coins
        