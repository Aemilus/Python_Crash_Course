"""Module for Bullet class."""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class for representing a bullet fired by the rocket."""
    def __init__(self, screen, rocket):
        """Bullet init."""
        super().__init__()
        self.screen = screen

        # settings
        self.width = 12
        self.height = 4
        self.color = (100, 220, 70)

        # make a rectangle for bullet
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # position the rectangle at tip of the rocket
        self.rect.centery = rocket.rect.centery
        self.rect.right = rocket.rect.right

    def update(self):
        """The bullet advances closer to right side of screen."""
        self.rect.right += 1

    def draw(self):
        """Draw the bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
