import pygame
import sys
from Alien_Invasion.chapter_12.settings import Settings
from Alien_Invasion.chapter_12.twelveSix_ship import Ship
from Alien_Invasion.chapter_12.twelveSix_bullet import Bullet


class SidewaysShooter:
    """Overall class to manage game behavior and assets"""

    def __init__(self):
        """Inits game and creates resources"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Sideways shooter")
        self.screen_rect = self.screen.get_rect()
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_keydown_events(self, event):
        """Checks for any keydown events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Checks for any keyup events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullets(self):
        """creates and fires bullets on the screen"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates position of bullets and draws/gets rid of old ones"""

        self.bullets.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _check_events(self):
        """Respond to keypress and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Updates img on screen and flips screen"""

        self.screen.fill(self.bg_color)
        self.ship.update()
        self.ship.blitme()
        self._update_bullets()
        pygame.display.flip()

    def start(self):
        """Starts the game"""

        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    ai = SidewaysShooter()
    ai.start()
