import sys
import pygame
from Alien_Invasion.chapter_12.twelveSix_bullet import Bullet
from Alien_Invasion.chapter_12.twelveSix_ship import Ship
from Alien_Invasion.chapter_13.thirteenFive_settings import Settings
from Alien_Invasion.chapter_13.thirteenFive_alien import Alien
from time import sleep
from Alien_Invasion.chapter_13.thirteenSix_gamestats import GameStats
from Alien_Invasion.chapter_14.fourteenOne_btn import Button
from Alien_Invasion.chapter_14.difficulty_btns import Button1, Button2, Button3
from Alien_Invasion.chapter_14.fourteenEight_scorebd import Scoreboard


class SidewaysShooter:
    """Overall class to manage game and attributes"""

    def __init__(self):
        """Inits all settings and attriubutes"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideways-Shooter 2")
        self.bg_color = self.settings.bg_color
        self.play_btn = Button(self, "Play")
        self.easy_btn = Button1(self, "Easy")
        self.medium_btn = Button2(self, "Medium")
        self.hard_btn = Button3(self, "Hard!")
        self.stats = GameStats(self)
        self.scorebd = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_alien(self, nr_aliens, nr_rows):
        """Creates instance of an alien"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = 200 + alien_width + 2 * alien_width * nr_rows
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * nr_aliens
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _create_fleet(self):
        """Creates fleet of aliens"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        available_space_x = self.settings.screen_width - (3 * alien_width) - ship_width
        nr_aliens_x = available_space_x // (2 * alien_width)
        available_space_y = self.settings.screen_height - (2 * alien_height)
        nr_rows = available_space_y // (2 * alien_height)
        for aliens in range(nr_aliens_x):
            for rows in range(nr_rows):
                self._create_alien(rows, aliens)

    def _check_edges(self):
        """checks whether aliens touch top or bottom of screen"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """changes direction of alien fleet"""

        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_left(self):
        """checks whether alien has reached left edge of screen"""

        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._ship_hit()

    def _ship_hit(self):
        """Respond to ship being hit by alien"""

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scorebd.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()

            sleep(1.0)
        else:
            self.stats.second_game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """updates aliens' position on screen"""

        self._check_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_left()

    def _fire_bullets(self):
        """creates and fires bullets on the screen"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """updates bullets on the screen"""

        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """check whether a bullet has hit an alien"""

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scorebd.prep_score()
            self.scorebd.check_high_scores()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scorebd.prep_level()
        self.bullets.update()

    def _check_keydown_events(self, event):
        """checks for any keydown events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            with open("highscoreThirteen.txt", "w") as f:
                f.write(str(self.stats.high_score))
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """checks for any keyup events"""

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_btn(self, mouse_pos):
        """Start new game when player clicks Play"""
        btn_clicked = self.play_btn.rect.collidepoint(mouse_pos)

        if btn_clicked and not self.stats.second_game_active:
            self.stats.reset_stats()
            self.stats.second_game_active = True
            self.scorebd.prep_score()
            self.scorebd.prep_level()
            self.scorebd.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            pygame.mouse.set_visible(False)

    def _check_easy_btn(self, mouse_pos):
        """Start new game when player clicks Play"""
        btn_clicked = self.easy_btn.rect.collidepoint(mouse_pos)

        if btn_clicked and not self.stats.second_game_active:
            self.settings.easy_speed()
            self.stats.reset_stats()
            self.stats.second_game_active = True
            self.scorebd.prep_score()
            self.scorebd.prep_level()
            self.scorebd.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            pygame.mouse.set_visible(False)

    def _check_medium_btn(self, mouse_pos):
        """Start new game when player clicks Play"""
        btn_clicked = self.medium_btn.rect.collidepoint(mouse_pos)

        if btn_clicked and not self.stats.second_game_active:
            self.settings.medium_speed()
            self.stats.reset_stats()
            self.stats.second_game_active = True
            self.scorebd.prep_score()
            self.scorebd.prep_level()
            self.scorebd.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            pygame.mouse.set_visible(False)

    def _check_hard_btn(self, mouse_pos):
        """Start new game when player clicks Play"""
        btn_clicked = self.hard_btn.rect.collidepoint(mouse_pos)

        if btn_clicked and not self.stats.second_game_active:
            self.settings.hard_speed()
            self.stats.reset_stats()
            self.stats.second_game_active = True
            self.scorebd.prep_score()
            self.scorebd.prep_level()
            self.scorebd.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            pygame.mouse.set_visible(False)

    def _check_events(self):
        """checks all events taking place"""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_btn(mouse_pos)
                self._check_easy_btn(mouse_pos)
                self._check_medium_btn(mouse_pos)
                self._check_hard_btn(mouse_pos)

    def _update_screen(self):
        """updates screen"""

        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()
        self.aliens.draw(self.screen)
        self.scorebd.show_score()
        if not self.stats.second_game_active:
            self.play_btn.draw_btn()
            self.easy_btn.draw_btn()
            self.medium_btn.draw_btn()
            self.hard_btn.draw_btn()
        pygame.display.flip()

    def run_game(self):
        """starts game and draws everything on the screen"""

        while True:
            self._check_events()
            if self.stats.second_game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


if __name__ == "__main__":
    game = SidewaysShooter()
    game.run_game()
