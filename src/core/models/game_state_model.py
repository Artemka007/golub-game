from typing import List
import pygame

from src.core.sprites.coin import Coin


class GameState:
    def __init__(self, player_position: pygame.Vector2, coins: List[Coin]):
        self.player_position = player_position
        self.coins = coins