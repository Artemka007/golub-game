import pygame


class PlatformView:
    def draw(self, surface: pygame.Surface, x: int, y: int, image: pygame.Surface):
        surface.blit(image, image.get_rect(topleft=(x, y)))