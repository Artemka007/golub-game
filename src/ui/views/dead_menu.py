import pygame
from src.core.utils.event_emitter import EventEmitter

from typing import Literal

from src.ui.factories.button import ButtonFactory
from src.ui.views.button import ButtonView


class DeadMenuView:
    def __init__(self, screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 16)
        buton_width = 200
        button_height = 44
        gap = 16
        first_y = (screen.get_height() - (button_height + gap)) / 2
        x = (screen.get_width() - buton_width) / 2
        self.buttons = [
            ButtonFactory.create_mvc_component(screen, pygame.Rect(x, first_y + button_height, buton_width, button_height), "Начать заново", self.font, lambda: emitter.emit('restart')),
        ]

    def draw(self, visible: bool):
        if not visible:
            return
        for btn in self.buttons:
            btn.draw()
