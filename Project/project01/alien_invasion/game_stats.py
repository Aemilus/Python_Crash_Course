class GameStats:
    """Track statistics for Alien Invasion game."""

    def __init__(self, ai_settings):
        """Init statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # start Alien Invasion game in an inactive state
        self.game_active = False
        # high score should never be reset
        self.high_score_filename = "highscore.json"
        self.load_high_score()

    def reset_stats(self):
        """Init statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open(self.high_score_filename, "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        try:
            with open(self.high_score_filename) as file:
                self.high_score = int(file.read().rstrip())
        except (IOError, ValueError, TypeError):
            self.high_score = 0
