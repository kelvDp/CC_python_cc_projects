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
        self.bullets_allowed = 8

        self.alien_speed = 1.5
        self.fleet_drop_speed = 10

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = -1
