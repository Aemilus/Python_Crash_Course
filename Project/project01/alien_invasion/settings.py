from game_sounds import LevelUpSound


class Settings:
    """Game settings."""

    def __init__(self):
        """Init game static settings."""
        # screen settings
        self.screen_height = 600
        self.screen_width = 1000
        self.bg_color = (10, 20, 50)
        # sound settings
        self.level_up_sound = LevelUpSound()
        # ship settings
        self.ship_limit = 3
        # bullet settings
        self.bullet_color = (60, 190, 255)
        self.bullets_allowed = 3
        self.bullet_width = 5
        self.bullet_height = 12
        # alien settings
        self.fleet_drop_speed = 40
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        # alien points multiplier at level progress
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init settings that change throughout the game."""
        self.ship_speed_factor = 0.6
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5
        # fleet direction of 1 represents right, -1 left
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
