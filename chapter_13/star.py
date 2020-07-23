from pygame.sprite import Sprite
import pygame


class Star(Sprite):
    """Class to make star"""

    def __init__(self, star_screen):
        """Inits star"""

        super().__init__()
        self.screen = star_screen.screen
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
