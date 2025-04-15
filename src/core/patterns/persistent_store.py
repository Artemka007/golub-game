from abc import ABC, abstractmethod
from src.core.patterns.stack import Stack


class PersistentStore[T](ABC):
    _stack: Stack[T]

    @abstractmethod
    def save(self): ...
    
    @abstractmethod
    def apply(self): ...
        