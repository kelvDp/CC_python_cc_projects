import sys
import pygame
from Alien_Invasion.chapter_12.tiy_rocket_settings import Settings
from Alien_Invasion.chapter_12.tiy_rocket import RImage


class Rocket:
    """Class to manage rocket behavior"""

    def __init__(self):
        """Initializes rocket"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket")
        self.bg_color = self.settings.bg_color
        self.ship = RImage(self)

    def _check_keydown_events(self, event):
        """Checks for any keydown events"""

        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks for keyup events"""

        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False


    def _check_events(self):
        """Checks for any event changes"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _update_screen(self):
        """Updates the screen"""

        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.ship.update()
        pygame.display.flip()

    def open_game(self):
        """Starts game"""

        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    rocket = Rocket()
    rocket.open_game()