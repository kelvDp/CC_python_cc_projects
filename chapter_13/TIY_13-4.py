import sys
import pygame
from Alien_Invasion.chapter_13.thirteenOne_settings import Settings
from Alien_Invasion.chapter_13.rain import Rain


class Raindrops:
    """Overall class to manage raindrops"""

    def __init__(self):
        """Inits raindrops + settings"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Steady rain")
        self.bg_color = (230, 230, 230)
        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()

    def _create_rain(self, nr_drops, nr_rows=0):
        """create instance of rain"""

        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * nr_drops
        rain.rect.x = rain.x
        rain.y = rain_height + 2 * rain_height * nr_rows
        rain.rect.y = rain.y
        self.raindrops.add(rain)

    def _create_raindrops(self):
        """creates raindrops"""

        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)
        nr_drops = available_space_x // (2 * rain_width)
        available_space_y = self.settings.screen_height - (2 * rain_height)
        nr_rows = available_space_y // (2 * rain_height)

        for rows in range(nr_rows):
            for drops in range(nr_drops):
                self._create_rain(drops, rows)

    def _new_row_drops(self):
        """creatse one new row of raindrops"""

        rain = Rain(self)
        rain_width = rain.rect.width
        available_x_space = self.settings.screen_width - (2 * rain_width)
        nr_of_drops = available_x_space // (2 * rain_width)
        for drops in range(nr_of_drops):
            self._create_rain(drops)

    def _update_raindrops(self):
        """Updates position of raindrops on screen"""

        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)
                self._new_row_drops()
        self.raindrops.update()

    def _update_screen(self):
        """Updates screen"""

        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
        self._update_raindrops()
        pygame.display.flip()

    def make_rain(self):
        """Draws raindrops to screen"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self._update_screen()


if __name__ == "__main__":
    r = Raindrops()
    r.make_rain()
