import pygame

from src.ui.models.button import ButtonModel
from src.ui.views.button import ButtonView


class ButtonController:
    def __init__(self, model: ButtonModel, view: ButtonView):
        self.model = model
        self.view = view

    def draw(self):
        self.view.draw(self.model)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.model.rect.collidepoint(event.pos):
                self.view.callback()