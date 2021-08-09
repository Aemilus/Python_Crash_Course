from random import randint

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Star(Sprite):
    """Class for a star."""
    # have some spacing around the star
    border = 35

    image = pygame.image.load("star.png")
    width = image.get_width()
    height = image.get_height()
    centerx = image.get_rect().centerx
    centery = image.get_rect().centery

    def __init__(self, screen, centerx, centery):
        super().__init__()
        self.screen = screen
        self.rect = Star.image.get_rect()

        # set star's position
        self.rect.centerx = centerx
        self.rect.centery = centery


class Stars(Group):
    """Class for a group of stars."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.number_rows = self.get_number_rows()
        self.number_cols = self.get_number_cols()
        self.add_stars()

    def get_number_rows(self):
        allowed_space_y = self.screen.get_rect().height - Star.border
        return int(allowed_space_y / (Star.height + Star.border))

    def get_number_cols(self):
        allowed_space_x = self.screen.get_rect().width - Star.border
        return int(allowed_space_x / (Star.width + Star.border))

    def add_stars(self):
        for row in range(self.number_rows):
            centery = (Star.border + Star.height) * row + Star.centery + Star.border
            for col in range(self.number_cols):
                rand_x = randint(-10, 10)
                rand_y = randint(-10, 10)
                centerx = (Star.border + Star.width) * col + Star.centerx + Star.border
                centerx += rand_x
                centery += rand_y
                star = Star(self.screen, centerx, centery)
                self.add(star)
