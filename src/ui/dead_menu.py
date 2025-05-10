import pygame
from src.core.patterns.event_emitter import EventEmitter
from src.ui.button import Button, WHITE

from typing import Literal


class DeadMenu:
    def __init__(self, screen: pygame.Surface, emitter: EventEmitter[Literal['restart', 'cancel']]):
        self.screen = screen
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 16)
        self.emitter = emitter
        buton_width = 200
        button_height = 44
        gap = 16
        first_y = (screen.get_height() - (button_height + gap)) / 2
        x = (screen.get_width() - buton_width) / 2
        self.buttons = [
            Button(pygame.Rect(x, first_y + button_height, buton_width, button_height), "Начать заново", lambda: self.emitter.emit('restart')),
        ]
        self.visible = False

    def draw(self):
        if not self.visible:
            return
        for btn in self.buttons:
            btn.draw(self.screen, self.font)

    def handle_event(self, event: pygame.event.Event):
        if not self.visible:
            return
        for btn in self.buttons:
            btn.handle_event(event)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False