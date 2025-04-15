from typing import Callable
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 100, 255)

class Button:
    def __init__(self, rect: pygame.Rect, text: str, callback: Callable):
        self.rect = rect
        self.text = text
        self.callback = callback
        self.color = GRAY

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()