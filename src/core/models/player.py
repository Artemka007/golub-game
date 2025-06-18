from typing import Literal

import pygame

from src.core.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.core.utils.event_emitter import EventEmitter


class PlayerModel:
    def __init__(self, emitter: EventEmitter[Literal['player_dead']]):
        self.image = pygame.image.load('./assets/images/sprite.png')
        original_width, original_height = self.image.get_size()
        new_size = (original_width // 10, original_height // 10)
        self.image = pygame.transform.scale(self.image, new_size)
        self.original_image = self.image
        self.rect = self.image.get_rect()

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

        self.velocity_y = 0
        self.velocity_x = 0

        self.is_jumping = False
        self.facing_right = True

        self.emitter = emitter

    def move(self, vector: pygame.Vector2):
        self.rect.x = vector.x
        self.rect.y = vector.y

        return self