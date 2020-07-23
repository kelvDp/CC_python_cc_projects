class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""

        self.settings = ai_game.settings

        # game active status for TIY_13-6
        self.game_active = True

        # game active status for TIY_14-1
        self.second_game_active = False

        self.ships_left = self.settings.ship_limit
