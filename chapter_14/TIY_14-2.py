import sys
import pygame
from Alien_Invasion.chapter_12.twelveSix_bullet import Bullet
from Alien_Invasion.chapter_12.twelveSix_ship import Ship
from Alien_Invasion.chapter_14.fourteenOne_btn import Button
from Alien_Invasion.chapter_14.fourteenTwo_settings import Settings
from Alien_Invasion.chapter_13.thirteenSix_gamestats import GameStats
from Alien_Invasion.chapter_14.target import Target


class TargetPractice:
    """Overall class to manage game and attributes"""

    def __init__(self):
        """Inits all settings and attriubutes"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Target Practice")
        self.bg_color = self.settings.bg_color
        self.btn = Button(self, "Press P to play")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

    def _fire_bullets(self):
        """creates and fires bullets on the screen"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """updates bullets on the screen"""

        self._bullet_target_collision()
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
                self.settings.max_bullets -= 1
                if self.settings.max_bullets == 0:
                    self.stats.second_game_active = False

    def _bullet_target_collision(self):
        """checks for collissions between bullets and target"""

        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.target.rect):
                self.bullets.remove(bullet)

    def _check_edges(self):
        """checks whether aliens touch top or bottom of screen"""

        self.target.check_edges()

    def _check_keydown_events(self, event):
        """checks for any keydown events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()
        if event.key == pygame.K_p:
            self.stats.second_game_active = True
            self.settings.max_bullets = 3
            pygame.mouse.set_visible(False)

    def _check_keyup_events(self, event):
        """checks for any keyup events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        """checks all events taking place"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """updates screen"""

        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()
        self.bullets.update()
        if not self.stats.second_game_active:
            self.btn.draw_btn()
        self.target.draw_target()
        self._check_edges()
        pygame.display.flip()

    def run_game(self):
        """starts game and draws everything on the screen"""

        while True:
            self._check_events()
            if self.stats.second_game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()
            self._update_screen()


if __name__ == "__main__":
    game = TargetPractice()
    game.run_game()
