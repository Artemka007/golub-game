from typing import List
import pygame

from src.core.controllers.platform import PlatformController
from src.core.constants import GRAVITY, JUMP_STRENGTH, PLAYER_SPEED
from src.core.models.player import PlayerModel
from src.core.utils.scene_model import Scene
from src.core.views.player import PlayerView


class PlayerController(pygame.sprite.Sprite):
    def __init__(self, model: PlayerModel, view: PlayerView):
        super().__init__()
        self.model = model
        self.view = view

    def update(self, scene):
        self.__handle_keypress()
        self.__handle_update_direction()
        self.__move_player(scene)
        self.__handle_borders(scene)
        self.view.draw(pygame.display.get_surface(), self.model.image, self.model.rect)

    def __move_player(self, scene):
        self.model.rect.x += self.model.velocity_x
        self.__handle_horizontal_collisions(scene.platforms)

        self.model.velocity_y += GRAVITY
        self.model.rect.y += int(self.model.velocity_y)
        self.__handle_vertical_collisions(scene.platforms)

    def __handle_keypress(self):
        keys = pygame.key.get_pressed()

        self.model.velocity_x = 0

        if keys[pygame.K_a]:
            self.model.velocity_x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.model.velocity_x = PLAYER_SPEED
        if keys[pygame.K_SPACE] and not self.model.is_jumping:
            self.model.velocity_y = JUMP_STRENGTH
            self.model.is_jumping = True

    def __handle_horizontal_collisions(self, platforms: List[PlatformController]):
        for platform in platforms:
            if not self.model.rect.colliderect(platform.model.rect):
                continue

            if self.model.velocity_x > 0: 
                self.model.rect.right = platform.model.rect.left

            if self.model.velocity_x < 0: 
                self.model.rect.left = platform.model.rect.right

    def __handle_vertical_collisions(self, platforms: List[PlatformController]):
        for platform in platforms:
            if not self.model.rect.colliderect(platform.model.rect):
                continue

            if self.model.velocity_y > 0: 
                self.model.rect.bottom = platform.model.rect.top
                self.model.velocity_y = 0
                self.model.is_jumping = False

            if self.model.velocity_y < 0: 
                self.model.rect.top = platform.model.rect.bottom
                self.model.velocity_y = 0

    def __handle_borders(self, scene: Scene):
        self.model.rect.left = max(0, self.model.rect.left)
        self.model.rect.right = min(scene.width, self.model.rect.right)
        
        if self.model.rect.top > scene.height:
            self.model.velocity_y = 0
            self.model.emitter.emit('player_dead')
            self.kill()

        if self.model.rect.top < 0:
            self.model.velocity_y = -self.model.velocity_y * 0.4

        self.model.rect.top = max(0, self.model.rect.top)

    def __handle_update_direction(self):
        if self.model.velocity_x < 0 and self.model.facing_right:
            self.model.image = self.model.original_image
            self.model.facing_right = False
            return

        if self.model.velocity_x > 0 and not self.model.facing_right:
            self.model.image = pygame.transform.flip(self.model.original_image, True, False)
            self.model.facing_right = True