from abc import ABC, abstractmethod
from typing import List


class Subject:
    def __init__(self):
        self._observers: List['Observer'] = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs): ...