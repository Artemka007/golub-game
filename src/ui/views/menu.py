import pygame
from src.core.utils.event_emitter import EventEmitter
from src.ui.button import Button, WHITE

from typing import List, Literal

from src.ui.factories.button import ButtonFactory


class MenuView:
    def __init__(self, screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 16)
        buton_width = 200
        button_height = 44
        gap = 16
        first_y = (screen.get_height() - (button_height + gap) * 3) / 2
        x = (screen.get_width() - buton_width) / 2
        self.buttons = [
            ButtonFactory.create_mvc_component(screen, pygame.Rect(x, first_y, buton_width, button_height), "Сохраниться", self.font, lambda: emitter.emit('save')),
            ButtonFactory.create_mvc_component(screen, pygame.Rect(x, first_y + button_height + gap, buton_width, button_height), "Начать заново", self.font, lambda: emitter.emit('restart')),
            ButtonFactory.create_mvc_component(screen, pygame.Rect(x, first_y + (button_height + gap) * 2, buton_width, button_height), "Закрыть", self.font, lambda: emitter.emit('cancel'))
        ]
        self.visible = False

    def draw(self, visible: bool):
        if not visible:
            return
        for btn in self.buttons:
            btn.draw()
