import sys
import pygame

from src.core.managers.coin_manager import CoinManager
from src.core.camera import Camera
from src.core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.core.sprites.player import Player
from src.scenes.level1 import Level1
from src.ui.coin_display import CoinDisplay


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Голубь в космосе")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load("./assets/images/background.jpg").convert()

        original_width, original_height = self.background.get_size()
        self.background = pygame.transform.scale(self.background, (original_width * 2, original_height * 2))

        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.camera = Camera()
        self.all_sprites.add(self.player)
        self.current_scene = Level1()
        self.coins_collected = 0

        self.coin_display = CoinDisplay()
        self.coin_manager = CoinManager(list(self.current_scene.coins))
        self.coin_manager.register_observer(self.coin_display)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__render_background()

            self.player.update(self.current_scene)
            self.coin_manager.update_player(self.player)

            self.camera.update(self.player, self.current_scene)
            self.screen.blit(self.player.image, self.camera.apply(self.player))

            for platform in self.current_scene.platforms:
                self.screen.blit(platform.image, self.camera.apply(platform))

            for coin in self.coin_manager.coins:
                coin.update()
                coin.draw(self.screen, self.camera)
            
            self.coin_display.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
    
    def __render_background(self):
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        offset_x = int(self.camera.offset.x // 3) % bg_width
        offset_y = int(self.camera.offset.y // 3) % bg_height

        for x in range(-offset_x - bg_width, SCREEN_WIDTH + bg_width, bg_width):
            for y in range(-offset_y - bg_height, SCREEN_HEIGHT + bg_height, bg_height):
                self.screen.blit(self.background, (x, y))