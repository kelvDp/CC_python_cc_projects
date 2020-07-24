import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create bullet object at ship's current location"""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self, *args):
        """Moves the bullets up the screen"""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullets(self):
        """Draws bullets onto the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
