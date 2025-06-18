from abc import ABC, abstractmethod


class Scene(ABC):
    _width: int
    _height: int

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @abstractmethod
    def update(self, *args, **kwargs): ...

    @abstractmethod
    def handle_event(self, *args, **kwargs): ...