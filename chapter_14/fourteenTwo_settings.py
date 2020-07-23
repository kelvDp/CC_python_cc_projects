from random import randint


class Settings:
    """A class to store all settings for game"""

    def __init__(self):
        """Inits the game settings"""

        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
        self.ship_limit = 2

        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.max_bullets = 3

        self.target_speed = 0.5
        self.target_width = 50
        self.target_height = 100
        self.target_color = (0, 250, 0)

    def update_speed(self):
        """updates speed of target"""
        self.target_speed += 0.3
        self.bullet_speed += 0.1
