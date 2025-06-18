import pygame
from src.core.utils.observable import Observable


class CoinDisplay:
    def __init__(self, coins_collected: Observable[int]):
        self.coins_collected = 0
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 36)
        self.coin_image = pygame.image.load('./assets/images/money.png')
        original_width, original_height = self.coin_image.get_size()
        new_size = (original_width // 2, original_height // 2)
        self.coin_image = pygame.transform.scale(self.coin_image, new_size)
        self.coins_collected_observable = coins_collected
        self.coins_collected_observable.subscribe(self.update)
    
    def __del__(self):
        self.coins_collected_observable.unsubscribe(self.update)

    def update(self, coins_collected):
        self.coins_collected = coins_collected

    def draw(self, screen: pygame.Surface):
        screen.blit(self.coin_image, (700, 10))
        font = pygame.font.Font(None, 32)
        text_surface = font.render(str(self.coins_collected), True, (255, 255, 255))
        screen.blit(text_surface, (740, 15))