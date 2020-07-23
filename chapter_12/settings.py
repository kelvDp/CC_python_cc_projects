# Each time we introduce new functionality into the game, we’ll typically
# create some new settings as well. Instead of adding settings throughout the
# code, let’s write a module called settings that contains a class called Settings to
# store all these values in one place.


class Settings:
    """A class to store all settings for game"""

    def __init__(self):
        """Inits the game settings"""

        # screen settings:
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings:
        # self.ship_speed = 1.5
        self.ship_limit = 2

        # bullet settings:
        # self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # alien settings:
        # self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # # fleet_direction of 1 represents right, -1 represents left
        # self.fleet_direction = 1

        # how quickly game speeds up:
        self.speedup_scale = 1.2

        # how quickly alien point values increase:
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # scoring:
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings + alien point values"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)