# we’ll create a new ship module that will contain the class Ship.
# This class will manage most of the behavior of the player’s ship:

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Inits ship and sets starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rectangle = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get its rectangle:
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rectangle.midbottom

        # store a decimal value for the ships' horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    # def update(self):
    #     """Update the ships' position based on movement flag"""
    #
    #     if self.moving_right:
    #         self.x += self.settings.ship_speed
    #     if self.moving_left:
    #         self.x -= self.settings.ship_speed
    #     self.rectangle.x = self.x
    #
    # def blitme(self):
    #     """Draw ship at its current location"""
    #     self.screen.blit(self.image, self.rectangle)

    def update(self):
        """Update the ships' position based on movement flag"""
        # we can stop the ship from going off of the screen:
        if self.moving_right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """Centers the ship on the screen"""

        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
