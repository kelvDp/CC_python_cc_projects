import pygame


class GameCharacter:
    """Overall class to blit character"""

    def __init__(self,window):
        """Inits the character"""

        self.screen = window.screen
        self.screen_rect = window.screen.get_rect()
        self.image = pygame.image.load("images/elephant-5402969_640.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_img(self):
        """Draws character on window"""

        self.screen.blit(self.image, self.rect)