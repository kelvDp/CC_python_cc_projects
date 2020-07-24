import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Overall class to manage ship"""

    def __init__(self, game):
        """Initializes ship and its attributes"""

        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updates ship position on screen"""

        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >= 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """centers ship on screen for starting position"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitship(self):
        """draws ship onto screen"""

        self.screen.blit(self.image, self.rect)
