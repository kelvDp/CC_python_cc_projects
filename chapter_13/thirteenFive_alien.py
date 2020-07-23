import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Inits alien and sets starting position"""

        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top

        self.y = float(self.rect.y)

    def check_edges(self):
        """Returns true if aliens are at edge of screen"""

        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """Move aliens to left or right"""

        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
