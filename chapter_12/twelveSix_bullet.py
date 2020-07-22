import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create bullet object at ship's current location"""

        super().__init__() # to init sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect.midleft = ai_game.ship.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        """Moves the bullet up the screen"""

        self.x += self.settings.bullet_speed
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draws the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
