import pygame

from src.core.models.scene_model import Scene
from src.core.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRAVITY, PLAYER_SPEED, JUMP_STRENGTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

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

    def update(self, scene: Scene):
        self.__handle_keypress()
        self.__handle_update_direction()

        self.rect.x += self.velocity_x
        self.__handle_horizontal_collisions(scene.platforms)

        self.velocity_y += GRAVITY
        self.rect.y += int(self.velocity_y)
        self.__handle_vertical_collisions(scene.platforms)

        self.__handle_borders(scene)
    
    def move(self, vector: pygame.Vector2):
        self.rect.x = vector.x
        self.rect.y = vector.y
    
    def __handle_keypress(self):
        keys = pygame.key.get_pressed()

        self.velocity_x = 0

        if keys[pygame.K_a]:
            self.velocity_x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.velocity_x = PLAYER_SPEED
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True

    def __handle_horizontal_collisions(self, platforms: pygame.sprite.Group):
        for platform in platforms:
            if not self.rect.colliderect(platform.rect):
                continue
            
            if self.velocity_x > 0: 
                self.rect.right = platform.rect.left
            
            if self.velocity_x < 0: 
                self.rect.left = platform.rect.right

    def __handle_vertical_collisions(self, platforms: pygame.sprite.Group):
        for platform in platforms:
            if not self.rect.colliderect(platform.rect):
                continue

            if self.velocity_y > 0: 
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.is_jumping = False

            if self.velocity_y < 0: 
                self.rect.top = platform.rect.bottom
                self.velocity_y = 0

    def __handle_borders(self, scene: Scene):
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(scene.width, self.rect.right)
        
        if self.rect.bottom > scene.height:
            self.velocity_y = 0
        
        if self.rect.top < 0:
            self.velocity_y = 0
        
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(scene.height, self.rect.bottom)

    def __handle_update_direction(self):
        if self.velocity_x < 0 and self.facing_right:
            self.image = self.original_image
            self.facing_right = False
            return
       
        if self.velocity_x > 0 and not self.facing_right:
            self.image = pygame.transform.flip(self.original_image, True, False)
            self.facing_right = True
