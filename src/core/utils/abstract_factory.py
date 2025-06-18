from abc import ABC, abstractmethod
from typing import TypeVar


M = TypeVar('M')
V = TypeVar('V')
C = TypeVar('C')


class AbstractMVCFactory[M, V, C](ABC):
    @staticmethod
    @abstractmethod
    def create_model(*args, **kwargs) -> M: ...

    @staticmethod
    @abstractmethod
    def create_view(*args, **kwargs) -> V: ...

    @staticmethod
    @abstractmethod
    def create_controller(model: M, view: V, *args, **kwargs) -> C: ...
    
    @staticmethod
    @abstractmethod
    def create_mvc_component(*args, **kwargs) -> C: ...