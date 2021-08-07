import pygame


class Ship:
    """Models a space ship."""

    def __init__(self, ai_settings, screen):
        """Initializes a ship and sets it's initial position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get it's rectangle
        self.image = pygame.image.load("images/small_rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store ship's centerx as a decimal value
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on movement flag."""
        # update the ship's center value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        # update ship's rect centerx value
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
