import pygame
from src.core.observer import Observer


class CoinDisplay(Observer):
    def __init__(self):
        self.coins_collected = 0
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 36)
        self.coin_image = pygame.image.load('./assets/images/money.png')
        original_width, original_height = self.coin_image.get_size()
        new_size = (original_width // 2, original_height // 2)
        self.coin_image = pygame.transform.scale(self.coin_image, new_size)

    def update(self, coins_collected):
        self.coins_collected = coins_collected

    def draw(self, screen: pygame.Surface):
        # Отображаем иконку монеты
        screen.blit(self.coin_image, (700, 10))  # Позиция иконки
        # Рисуем рядом количество собранных монет
        font = pygame.font.Font(None, 32)  # Можно использовать шрифт поменьше
        text_surface = font.render(str(self.coins_collected), True, (255, 255, 255))
        screen.blit(text_surface, (740, 15))  # Позиция текста рядом с иконкой