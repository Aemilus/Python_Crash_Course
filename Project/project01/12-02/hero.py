import pygame


class Hero:
    """A class for a hero character in a game."""

    def __init__(self, screen):
        # set screen
        self.screen = screen
        # get screen rect
        self.screen_rect = screen.get_rect()
        # load hero image
        self.image = pygame.image.load("knight.png")
        # get hero image rect
        self.rect = self.image.get_rect()
        # set position of hero image rect at center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw hero on screen."""
        self.screen.blit(self.image, self.rect)
