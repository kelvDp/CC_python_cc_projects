import pygame.font
from pygame.sprite import Group
from Alien_Invasion.final_version.ship import Ship


class ScoreBoard:
    """A class to report scoring information"""

    def __init__(self, game):
        """Initializes scorekeeping attributes"""

        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.txt_color = (255, 255, 204)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """turns score into rendered img"""

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_img = self.font.render(score_str, True, self.txt_color, self.settings.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """turns high_score into a rendered img"""

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.txt_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """turns level into rendered img"""

        level_str = f"Level {self.stats.level}"
        self.level_img = self.font.render(level_str, True, self.txt_color, self.settings.bg_color)

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """shows the amount of ships player has left"""

        self.ships = Group()
        for ship_nr in range(self.stats.ships_left + 1):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_nr * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_scores(self):
        """checks to see if there is an updated high score"""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """draws score onto screen"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)
