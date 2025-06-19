import pygame
from src.core.utils.observable import Observable


class CoinDisplayView:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
    
    def draw(self, coin_image: pygame.Surface, coins_collected: int):
        self.screen.blit(coin_image, (700, 10))
        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(coins_collected), True, (255, 255, 255))
        self.screen.blit(text_surface, (740, 15))