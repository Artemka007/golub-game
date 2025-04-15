import pygame


class Scene:
    _width: int
    _height: int

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height