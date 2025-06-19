import pygame

from src.ui.models.menu import MenuModel
from src.ui.views.menu import MenuView


class MenuController:
    def __init__(self, model: MenuModel, view: MenuView):
        self.model = model
        self.view = view

    def draw(self):
        self.view.draw(self.model.visible)

    def handle_event(self, event: pygame.event.Event):
        if not self.model.visible:
            return
        for btn in self.view.buttons:
            btn.handle_event(event)