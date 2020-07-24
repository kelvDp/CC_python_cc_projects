import pygame


class Settings:
    """A class to store and manage all game settings"""

    def __init__(self):
        """Initializes all game settings"""

        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 25, 51)

        self.ship_limit = 2

        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 51, 51)
        self.bullets_allowed = 4

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2

        self.score_scale = 1.5

        self.reset_dynamic_settings()

    def reset_dynamic_settings(self):
        """Resets all dynamic settings of game"""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_score = 50

    def increase_speed(self):
        """Increases speed of game and score values"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.score_scale)

    def easy_speed(self):
        """starts game off with easy speed"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

    def medium_speed(self):
        """starts game off with easy speed"""
        self.ship_speed = 2.0
        self.bullet_speed = 3.5
        self.alien_speed = 2.0

    def hard_speed(self):
        """starts game off with easy speed"""
        self.ship_speed = 2.5
        self.bullet_speed = 4.0
        self.alien_speed = 4.0
