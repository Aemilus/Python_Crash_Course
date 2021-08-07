"""Module for Rocket class."""

import pygame
from pygame.sprite import Group

from bullet import Bullet


class Rocket:
    """Class for representing a rocket."""
    def __init__(self, screen):
        """Rocket init."""
        self.screen = screen
        self.image = pygame.image.load("rocket_left_side.png")
        self.rect = self.image.get_rect()

        # set initial position
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # movement flags
        self.moving_up = False
        self.moving_down = False

        # bullets for the rocket
        self.bullets = Group()
        self.max_bullets = 3

    def blitme(self):
        """Draw the rocket on screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update rocket state and it's components."""
        # update rocket
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.top -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1

    def update_bullets(self):
        """Update bullets inventory and position."""
        # remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        # update remaining bullets
        self.bullets.update()

    def fire_bullet(self):
        """
        Fires a bullet from rocket.
        Maximum 3 bullets can be launched.
        When one of the bullets is no longer on the screen then a new bullet can be fired.
        """
        if len(self.bullets) < 3:
            bullet = Bullet(self.screen, self)
            self.bullets.add(bullet)

    def draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw()
