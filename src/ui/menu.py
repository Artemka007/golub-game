import pygame
from src.core.patterns.event_emitter import EventEmitter
from src.ui.button import Button, WHITE

from typing import Literal


class Menu:
    def __init__(self, screen: pygame.Surface, emitter: EventEmitter[Literal['save', 'restart', 'cancel']]):
        self.screen = screen
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 16)
        self.emitter = emitter
        self.buttons = [
            Button(pygame.Rect(120, 100, 200, 60), "Сохраниться", lambda: self.emitter.emit('save')),
            Button(pygame.Rect(120, 200, 200, 60), "Начать заново", lambda: self.emitter.emit('restart')),
            Button(pygame.Rect(120, 300, 200, 60), "Закрыть", lambda: self.emitter.emit('cancel'))
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