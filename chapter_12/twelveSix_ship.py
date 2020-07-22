# we’ll create a new ship module that will contain the class Ship.
# This class will manage most of the behavior of the player’s ship:

import pygame


class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Inits ship and sets starting position"""

        self.screen = ai_game.screen
        self.screen_rectangle = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image and get its rectangle:
        self.image = pygame.image.load("images/rotatedShip.bmp")
        self.rect = self.image.get_rect()
        # start each new ship at bottom center of screen
        self.rect.midleft = self.screen_rectangle.midleft

        # store a decimal value for the ships' horizontal position
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ships' position based on movement flag"""

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rectangle.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def center_ship(self):
        """Centers the ship on the screen"""

        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
