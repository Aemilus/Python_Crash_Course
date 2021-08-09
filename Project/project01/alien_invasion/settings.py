class Settings:
    """Game settings."""

    def __init__(self):
        """A class to store game settings."""
        self.screen_height = 600
        self.screen_width = 1000
        self.bg_color = (10, 20, 50)
        # ship settings
        self.ship_speed_factor = 0.6
        self.ship_limit = 3
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 190, 255)
        self.bullets_allowed = 3
        self.bullet_width = 5
        self.bullet_height = 12
        # alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 40
        # fleet direction of 1 represents right, -1 left
        self.fleet_direction = 1
