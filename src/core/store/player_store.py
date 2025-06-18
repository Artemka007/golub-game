import pygame
from src.core.controllers.player import PlayerController
from src.core.utils.persistent_store import PersistentStore


class PlayerState:
    def __init__(self, position: pygame.Vector2):
        self.position = position


class PlayerStore(PersistentStore[PlayerState]):
    def __init__(self, player: PlayerController):
        super().__init__()
        self._player = player
    
    def save(self):
        self._stack.push(
            PlayerState(
                pygame.Vector2(
                    self._player.model.rect.x, 
                    self._player.model.rect.y
                )
            )
        )
    
    def undo(self):
        if self._stack.empty():
            return
        
        self._player.model.move(self._stack.pop().position)
        