class GameStats:
    """Overall class to handle game stats"""

    def __init__(self, game):
        """Initializes game stats"""

        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

        with open("AI-high_score.txt") as f:
            score = f.readline()
        self.high_score = int(score)

    def reset_stats(self):
        """Resets stats that change during game"""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
