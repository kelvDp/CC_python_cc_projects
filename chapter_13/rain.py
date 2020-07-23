from pygame.sprite import Sprite
import pygame


class Rain(Sprite):
    """Class to make raindrops"""

    def __init__(self, game):
        """Inits raindrops and its attributes"""

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("images/drop.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if drops are at bottom of screen"""

        if self.rect.bottom > self.screen_rect.bottom:
            return True

    def update(self):
        """Updates position of rain on screen"""

        self.y += self.settings.speed
        self.rect.y = self.y
