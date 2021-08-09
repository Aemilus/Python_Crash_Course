class GameStats:
    """Track statistics for Alien Invasion game."""
    def __init__(self, ai_settings):
        """Init statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # start Alien Invasion game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Init statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        