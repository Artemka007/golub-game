from typing import Literal
import pygame
from src.core.camera import Camera
from src.core.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.core.models.level import LevelModel
from src.core.utils.event_emitter import EventEmitter
from src.ui.coin_display import CoinDisplay
from src.ui.dead_menu import DeadMenu
from src.ui.menu import Menu


class LevelView:
    def __init__(self, model: LevelModel, screen: pygame.Surface, emitter: EventEmitter[Literal['save', 'restart', 'cancel', 'player_dead']]):
        self.screen = screen
        self.menu = Menu(screen, emitter)
        self.dead_menu = DeadMenu(screen, emitter)
        self.background = pygame.image.load("./assets/images/background.jpg").convert()
        original_width, original_height = self.background.get_size()
        self.background = pygame.transform.scale(self.background, (original_width * 2, original_height * 2))
        self.coin_display = CoinDisplay(model.coins_store.coins_collected)
        self.model = model
        self.emitter = emitter

    def draw(self, model: LevelModel):
        if self.menu.visible:
            self.menu.draw()
            return

        self.draw_background(model.camera)
        
        self.screen.blit(model.player.model.image, model.camera.apply(model.player.model))
        for platform in model.platforms:
            self.screen.blit(platform.model.image, model.camera.apply(platform.model))

        for coin in model.coins:
            coin.update()
            coin.draw(self.screen, model.camera)

        self.coin_display.draw(self.screen)
        self.menu.draw()
        self.dead_menu.draw()

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if self.menu.visible:
                self.menu.hide()
            else:
                self.menu.show()
        self.menu.handle_event(event)
        self.dead_menu.handle_event(event)
        
    
    def draw_background(self, camera: Camera):
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        offset_x = int(camera.offset.x // 3) % bg_width
        offset_y = int(camera.offset.y // 3) % bg_height

        for x in range(-offset_x - bg_width, SCREEN_WIDTH + bg_width, bg_width):
            for y in range(-offset_y - bg_height, SCREEN_HEIGHT + bg_height, bg_height):
                self.screen.blit(self.background, (x, y))
    
    def reset(self, model: LevelModel):
        self.__init__(model, self.screen, self.emitter)