from typing import Callable
import pygame


GRAY = (200, 200, 200)


class ButtonModel:
    def __init__(self, rect: pygame.Rect, text: str, font: pygame.font.Font):
        self.rect = rect
        self.text = text
        self.color = GRAY
        self.font = font
