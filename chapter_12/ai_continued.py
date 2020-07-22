import sys
import pygame
from Alien_Invasion.chapter_12.settings import Settings  # import setting class to use
from Alien_Invasion.chapter_12.ship import Ship
from Alien_Invasion.chapter_12.bullet import Bullet
from Alien_Invasion.chapter_13.alien import Alien
from time import sleep
from Alien_Invasion.chapter_13.game_stats import GameStats
from Alien_Invasion.chapter_14.button import Button
from Alien_Invasion.chapter_14.scoreboard import Scoreboard


# Pygame creates a black screen by default, but that’s boring. Let’s set a
# different background color. We’ll do this at the end of the __init__() method.

# class AlienInvasion:
#     """Overall class to manage game behavior and assets"""
#
#     def __init__(self):
#         """Init game and create resources"""
#
#         pygame.init()
#         self.screen = pygame.display.set_mode((1200, 800))
#         pygame.display.set_caption("Alien Invasion")
#         # set bg color:
#         self.bg_color = (230, 230, 230) # Colors in Pygame are specified as RGB colors
#
#     def run_game(self):
#         """Starts the game"""
#
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
#             # redraw screen during each pass through loop
#             self.screen.fill(self.bg_color)
#             # make recent drawn screen visible
#             pygame.display.flip()
# we fill the screen with the background color using the fill() method, which acts on a surface
# and takes only one argument: a color.

# --------------------------------------------------------------------------

class AlienInvasion:
    """Overall class to manage game behavior and assets"""

    def __init__(self):
        """Init game and create resources"""
        # To run the game in fullscreen mode, make the following changes in
        # __init__():*

        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # *
        self.settings.screen_width = self.screen.get_rect().width  # *
        self.settings.screen_height = self.screen.get_rect().height  # *
        pygame.display.set_caption("Alien Invasion")

        # create an instance to store game stats:
        self.stats = GameStats(self)
        self.scorebd = Scoreboard(self)

        # create ship:
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # set bg color:
        self.bg_color = self.settings.bg_color  # Colors in Pygame are specified as RGB colors

        # make play button:
        self.play_btn = Button(self, "Play")

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # make an alien and find nr of aliens in a row
        # spacing between aliens is == one alien width

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine nr of rows of aliens that fit on screen

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # create first row of aliens
        # for alien_number in range(number_aliens_x):
        #     self._create_alien(alien_number)
        # create full fleet of aliens:
        for row_nr in range(number_rows):
            for alien_nr in range(number_aliens_x):
                self._create_alien(alien_nr, row_nr)

    def _create_alien(self, alien_number, row_nr):
        """Creates alien + place it in row"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_nr
        self.aliens.add(alien)

    def _update_aliens(self):
        """Updates aliens' position on screen"""

        self._check_fleet_edges()
        self.aliens.update()

        # look for alien0ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!")
            self._ship_hit()

        # look for aliens hitting bottom of screen:
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Responds appropriately if aliens have reached an edge"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop fleet and change their direction"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to ship being hit by alien"""

        if self.stats.ships_left > 0:
            # decrement ships_left
            self.stats.ships_left -= 1
            self.scorebd.prep_ships()

            # get rid of any remaining aliens and bullets:
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and center ship:
            self._create_fleet()
            self.ship.center_ship()

            # Pause game for a bit:
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Checks if aliens reached bottom of screen"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as ship being hit
                self._ship_hit()
                break

    def _check_play_btn(self, mouse_pos):
        """Start new game when player clicks Play"""
        btn_clicked = self.play_btn.rect.collidepoint(mouse_pos)

        if btn_clicked and not self.stats.game_active:
            # reset game stats:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scorebd.prep_score()
            self.scorebd.prep_level()
            self.scorebd.prep_ships()

            # reset game settings:
            self.settings.initialize_dynamic_settings()

            # get rid of remaining aliens + bullets
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet
            self._create_fleet()
            self.ship.center_ship()

            # hide mouse cursor:
            pygame.mouse.set_visible(False)

    def run_game(self):
        """Starts the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_SPACE:
                        if len(self.bullets) < self.settings.bullets_allowed:
                            new_bullet = Bullet(self)
                            self.bullets.add(new_bullet)  # -> ads to bullet/sprite group

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_q:
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self._check_play_btn(mouse_position)

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()  # --> calls bullet.update() for each bullet we place in the group bullets.

                # get rid of bullets that have dissappeared:
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)

                # redraw screen during each pass through loop
                self.screen.fill(self.bg_color)
                # draw ship:
                self.ship.blitme()

                # draws bullets to screen :
                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()

                # checks for any bullets that have hit aliens:
                # if yes, get rid of bullet and alien:
                collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
                if collisions:
                    for aliens in collisions.values():
                        self.stats.score += self.settings.alien_points * len(aliens)

                    self.scorebd.prep_score()
                    self.scorebd.check_high_scores()
                # two True arguments tell Pygame to
                # delete the bullets and aliens that have collided.
                # To make a high-powered
                # bullet that can travel to the top of the screen, destroying every alien in its
                # path, you could set the first Boolean argument to False and keep the second
                # Boolean argument set to True. The aliens hit would disappear, but all bullets
                # would stay active until they disappeared off the top of the screen.)

                if not self.aliens:
                    # Destroy existing bullets and create new fleet
                    self.bullets.empty()
                    self._create_fleet()
                    self.settings.increase_speed()

                    # increase level:
                    self.stats.level += 1
                    self.scorebd.prep_level()

                self.aliens.draw(self.screen)  # -->
                # method requires
                # one argument: a surface on which to draw the elements from the group

                # draw score info:
                self.scorebd.show_score()

                self._update_aliens()

            # draw play btn if game inactive:
            if not self.stats.game_active:
                self.play_btn.draw_btn()

            # make recent drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
