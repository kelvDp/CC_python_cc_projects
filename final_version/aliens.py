import pygame
from pygame.sprite import Sprite


class Aliens(Sprite):
    """Overall class to manage alien behavior and assets"""

    def __init__(self, game):
        """Initializes aliens and their attributes"""

        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("images/ufo.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns true if aliens reach edges of screen"""

        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Updates aliens' position on screen"""

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
