import pygame
from Alien_Invasion.chapter_12.tiy_rocket_settings import Settings


class RImage:
    """Class to make the rocket"""

    def __init__(self, rocket):
        """inits the rocket"""

        self.settings = Settings()
        self.screen = rocket.screen
        self.screen_rect = rocket.screen.get_rect()
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """Updates ship position on screen"""

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draws the rocket"""

        self.screen.blit(self.image, self.rect)
