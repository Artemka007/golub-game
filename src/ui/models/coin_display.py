import pygame


class CoinDisplayModel:
    def __init__(self):
        self.coins_collected = 0
        self.font = pygame.font.Font('./assets/fonts/Roboto.ttf', 36)
        self.coin_image = pygame.image.load('./assets/images/money.png')
        original_width, original_height = self.coin_image.get_size()
        new_size = (original_width // 2, original_height // 2)
        self.coin_image = pygame.transform.scale(self.coin_image, new_size)