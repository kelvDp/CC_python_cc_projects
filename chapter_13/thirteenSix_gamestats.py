class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""

        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        # game active status for TIY_14-1
        self.second_game_active = False

        # high scores should never be reset:
        with open("highscoreThirteen.txt") as f:
            score = int(f.readline())
        self.high_score = score

    def reset_stats(self):
        """Inits stats that can change during game"""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
