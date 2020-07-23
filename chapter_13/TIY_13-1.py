import pygame
import sys
from Alien_Invasion.chapter_13.thirteenOne_settings import Settings
from Alien_Invasion.chapter_13.star import Star


class Stars:
    """Overall class to make stars"""

    def __init__(self):
        """Inits the stars and settings and sets starting position"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()
        self._create_sky_of_stars()

    def _create_star(self, star_nr, row_nr):
        """create one star"""

        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_nr
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_nr
        self.stars.add(star)

    def _create_sky_of_stars(self):
        """Creates a bunch of stars on the screen"""

        star = Star(self)
        star_width, star_height = star.rect.size
        available_x_space = self.settings.screen_width - (2 * star_width)
        star_number = available_x_space // (2 * star_width)

        available_y_space = self.settings.screen_height - (2 * star_height)
        number_of_rows = available_y_space // (2 * star_height)

        for row_nr in range(number_of_rows):
            for star_nr in range(star_number):
                self._create_star(star_nr, row_nr)

    def make_sky(self):
        """Creates pygame window with stars"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.stars.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    s = Stars()
    s.make_sky()






