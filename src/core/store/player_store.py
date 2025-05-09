import pygame
from src.core.models.player_state import PlayerState
from src.core.patterns.persistent_store import PersistentStore
from src.core.sprites.player import Player


class PlayerStore(PersistentStore[PlayerState]):
    def __init__(self, player: Player):
        super().__init__()
        self._player = player
    
    def save(self):
        self._stack.push(
            PlayerState(
                pygame.Vector2(
                    self._player.rect.x, 
                    self._player.rect.y
                )
            )
        )
    
    def undo(self):
        if self._stack.empty():
            return
        
        self._player.move(self._stack.pop().position)
        