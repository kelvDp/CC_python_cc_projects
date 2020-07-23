class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""

        self.settings = ai_game.settings
        self.reset_stats()

        # # start game in an active state:
        # self.game_active = True

        # start game in an inactive position:
        self.game_active = False

        # high scores should never be reset:
        self.high_score = 0

    def reset_stats(self):
        """Inits stats that can change during game"""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

