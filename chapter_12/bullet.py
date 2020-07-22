import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create bullet object at ship's current location"""

        super().__init__()  # to init sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # The bullet isn’t based on an
        # image, so we have to build a rect from scratch using the pygame.Rect() class.
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullets' position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up the screen"""

        # update the decimal position of bullet:
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
