from random import randint

import pygame
from pygame.sprite import Sprite


class Catcher(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("img/man.png")
        # set initial position
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # movement flags
        self.moving_left = False
        self.moving_right = False
        self.move_speed = 0.7
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.move_speed
            self.rect.x = self.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.move_speed
            self.rect.x = self.x


class Ball(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("img/ball.png")
        # set initial position at random
        self.rect = self.image.get_rect()
        self.rect.top = 10
        self.rect.left = randint(self.screen_rect.left, self.screen_rect.width - self.rect.width)
        # movement
        self.drop_speed = 0.3
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y
