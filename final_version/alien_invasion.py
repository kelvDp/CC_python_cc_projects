import sys
import pygame
from time import sleep
from Alien_Invasion.final_version.ship import Ship
from Alien_Invasion.final_version.aliens import Aliens
from Alien_Invasion.final_version.bullets import Bullets
from Alien_Invasion.final_version.game_stats import GameStats
from Alien_Invasion.final_version.scoreboard import ScoreBoard
from Alien_Invasion.final_version.game_settings import Settings
from Alien_Invasion.final_version.buttons import EasyBtn, MediumBtn, HardBtn
from Alien_Invasion.final_version.sounds import Sounds


class AlienInvasion:
    """Overall class to manage game and assets"""

    def __init__(self):
        """Initializes game and all attributes"""

        pygame.init()
        self.sounds = Sounds()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.scorebd = ScoreBoard(self)
        self.easy_btn = EasyBtn(self, "Easy")
        self.med_btn = MediumBtn(self, "Medium")
        self.hard_btn = HardBtn(self, "Hard")
        self._create_fleet()

    def _create_alien(self, alien_nr, row_nr):
        """Creates an alien and places it in a row"""

        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width) * alien_nr
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien_height) * row_nr
        self.aliens.add(alien)

    def _create_fleet(self):
        """Creates fleet of aliens"""

        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        available_x_space = self.settings.screen_width - (2 * alien_width)
        nr_aliens = available_x_space // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_y_space = self.settings.screen_height - (3 * alien_height) - ship_height
        nr_rows = available_y_space // (2 * alien_height)

        for row in range(nr_rows):
            for alien in range(nr_aliens):
                self._create_alien(alien, row)

    def _check_fleet_edges(self):
        """checks to see if aliens hit edges of screen"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """changes direction of aliens"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """check to see if aliens have reached bottom of screen"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        """updates aliens' position on screen"""

        self._check_fleet_edges()
        self._check_aliens_bottom()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """respond to ship being hit by aliens"""

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scorebd.prep_ship()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.sounds.collideSound.play()

            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _fire_bullets(self):
        """creates and fires bullets on screen"""

        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullets(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        """updates position and draws or gets rid of bullets"""

        self._check_bullet_alien_collision()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collision(self):
        """remove bullets and aliens that have collided"""

        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collision:
            for alien in collision.values():
                self.stats.score += self.settings.alien_score * len(alien)
            self.sounds.hitSound.play()
            self.scorebd.prep_score()
            self.scorebd.check_high_scores()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scorebd.prep_level()

        self.bullets.update()

    def _update_screen(self):
        """updates all images on screen and flips display"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.aliens.draw(self.screen)
        self.scorebd.show_score()

        if not self.stats.game_active:
            self.easy_btn.draw_btn()
            self.med_btn.draw_btn()
            self.hard_btn.draw_btn()

        pygame.display.flip()

    def _check_keydown_events(self, event):
        """checks for any keydown events happening"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self.sounds.bulletSound.play()
            self._fire_bullets()
        if event.key == pygame.K_q:
            with open("AI-high_score.txt", "w") as f:
                f.write(str(self.stats.high_score))
            sys.exit()

    def _check_keyup_events(self, event):
        """checks for any keyup events happening"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_easy_btn(self, mouse_pos):
        """start new game on easy difficulty"""

        btn_clicked = self.easy_btn.rect.collidepoint(mouse_pos)
        if btn_clicked and not self.stats.game_active:
            self.settings.easy_speed()
            self.reset_game()

    def _check_med_btn(self, mouse_pos):
        """start new game on medium difficulty"""

        btn_clicked = self.med_btn.rect.collidepoint(mouse_pos)
        if btn_clicked and not self.stats.game_active:
            self.settings.medium_speed()
            self.reset_game()

    def _check_hard_btn(self, mouse_pos):
        """start new game on hard difficulty"""

        btn_clicked = self.hard_btn.rect.collidepoint(mouse_pos)
        if btn_clicked and not self.stats.game_active:
            self.settings.hard_speed()
            self.reset_game()

    def _check_events(self):
        """checks all events taking place"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_easy_btn(mouse_pos)
                self._check_med_btn(mouse_pos)
                self._check_hard_btn(mouse_pos)

    def run_game(self):
        """starts game and draws everything on the screen"""

        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def reset_game(self):
        """resets all stats (except highscore) and restarts game"""

        self.stats.reset_stats()
        self.stats.game_active = True
        self.scorebd.prep_score()
        self.scorebd.prep_level()
        self.scorebd.prep_ship()
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
