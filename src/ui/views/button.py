from typing import Callable
import pygame

from src.ui.models.button import ButtonModel


BLACK = (0, 0, 0)


class ButtonView:
    def __init__(self, screen: pygame.Surface, callback: Callable):
        self.screen = screen
        self.callback = callback
    
    def draw(self, model: ButtonModel):
        pygame.draw.rect(self.screen, model.color, model.rect)
        text_surf = model.font.render(model.text, True, BLACK)
        text_rect = text_surf.get_rect(center=model.rect.center)
        self.screen.blit(text_surf, text_rect)