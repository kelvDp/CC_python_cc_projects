import sys
import pygame
from Alien_Invasion.chapter_13.thirteenOne_settings import Settings
from Alien_Invasion.chapter_13.rain import Rain


class RainDrop:
    """Overall class to make raindrops"""

    def __init__(self):
        """Inits raindrops and settings"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")
        self.bg_color = (230, 230, 230)
        self.raindrops = pygame.sprite.Group()
        self._creat_rain()

    def _create_raindrop(self, rain_nr, row_nr):
        """Creates an instance of rain"""

        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * rain_nr
        rain.rect.x = rain.x
        rain.y = rain_height + 2 * rain_height * row_nr
        rain.rect.y = rain.y
        self.raindrops.add(rain)

    def _creat_rain(self):
        """Creates raindrops"""

        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)
        nr_rain_x = available_space_x // (2 * rain_width)

        available_space_y = self.settings.screen_height - rain_height
        nr_of_rows = available_space_y // (2 * rain_height)

        for rows in range(nr_of_rows):
            for rain in range(nr_rain_x):
                self._create_raindrop(rain, rows)

    def _update_rain(self):
        """updates position of rain on screen"""
        for rain in self.raindrops.sprites():
            if rain.check_edges():
                self.raindrops.remove(rain)
        self.raindrops.update()

    def make_rain(self):
        """draws rain on screen"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self._update_rain()
            self.raindrops.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    r = RainDrop()
    r.make_rain()
