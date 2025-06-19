import pygame
from src.core.utils.event_emitter import EventEmitter
from src.ui.button import Button, WHITE

from typing import Literal

from src.ui.models.dead_menu import DeadMenuModel
from src.ui.views.dead_menu import DeadMenuView


class DeadMenuController:
    def __init__(self, model: DeadMenuModel, view: DeadMenuView):
        self.model = model
        self.view = view

    def draw(self):
        self.view.draw(self.model.visible)

    def handle_event(self, event: pygame.event.Event):
        if not self.model.visible:
            return
        for btn in self.view.buttons:
            btn.handle_event(event)
