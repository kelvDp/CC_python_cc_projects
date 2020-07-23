import pygame


class Target:
    """Overall class to manage a target and it's settings"""

    def __init__(self, game):
        """Inits target and attributes"""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.color = self.settings.target_color
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = True

    def update(self):
        """Updates position of target on screen"""

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.target_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.target_speed
        self.rect.y = self.y

    def check_edges(self):
        """Returns true if target is at bottom of screen"""

        if self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
            self.moving_up = True
        elif self.rect.top <= 0:
            self.moving_up = False
            self.moving_down = True

    def draw_target(self):
        """draws target on screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)
