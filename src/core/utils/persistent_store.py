from abc import ABC, abstractmethod
from typing import TypeVar
from src.core.utils.stack import Stack


T = TypeVar('T')


class PersistentStore[T](ABC):
    _stack: Stack[T]

    def __init__(self, *args, **kwargs):
        self._stack = Stack[T]()

    @abstractmethod
    def save(self): ...
    
    @abstractmethod
    def undo(self): ...
        