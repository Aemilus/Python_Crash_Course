from time import sleep

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Rocket(Sprite):
    image = pygame.image.load("rocket.png")
    speed_factor = 0.5
    max_bullets = 3

    def __init__(self, game, screen):
        super().__init__()
        self.game = game
        self.rect = Rocket.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        # movement attributes
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        # bullets
        self.bullets = Bullets(self.game)

    def update(self):
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= Rocket.speed_factor
            self.rect.y = self.y
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += Rocket.speed_factor
            self.rect.y = self.y

    def fire_bullet(self):
        if len(self.bullets) < Rocket.max_bullets:
            bullet = Bullet(self.screen, self)
            self.bullets.add(bullet)

    def draw_rocket(self):
        self.screen.blit(Rocket.image, self.rect)


class Bullet(Sprite):
    color = (100, 50, 3)
    speed_factor = 1

    def __init__(self, screen, rocket):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 5)
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery
        self.x = float(self.rect.x)

    def update(self):
        self.x += Bullet.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, Bullet.color, self.rect)


class Bullets(Group):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def draw_bullets(self):
        for bullet in self.sprites():
            bullet.draw_bullet()

    def update_bullets(self):
        self.update()
        # if bullet is not visible anymore then remove it from group
        # this also means that the player has lost a life
        for bullet in self.sprites()[:]:  # for some reason self.copy() gives error
            if bullet.rect.left >= bullet.screen.get_rect().right:
                self.game.rocket_lives -= 1
                self.remove(bullet)


class Target(Sprite):
    color = (200, 100, 50)
    speedup_factor = 0.1

    def __init__(self, game, screen):
        super().__init__()
        self.game = game
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 30, 170)
        self.rect.right = self.screen.get_rect().right - 10
        self.rect.centery = self.screen.get_rect().centery
        self.y = float(self.rect.y)
        self.speed_factor = 0.3
        self.hits = 0

    def update(self):
        # reverse direction if reached the top or bottom
        if self.rect.top <= self.screen.get_rect().top:
            self.speed_factor *= -1
        elif self.rect.bottom >= self.screen.get_rect().bottom:
            self.speed_factor *= -1
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, Target.color, self.rect)


class Button:
    def __init__(self, screen, text):
        # screen attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # button dimensions
        self.width = 200
        self.height = 60
        self.button_color = (125, 0, 200)
        # text attributes
        self.text = text
        self.text_color = (240, 240, 240)
        self.font = pygame.font.SysFont(None, 40)
        # button rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # render text and center on button
        self.text_render = self.font.render(self.text, True, self.text_color, self.button_color)
        self.text_render_rect = self.text_render.get_rect()
        self.text_render_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_render, self.text_render_rect)


class GameStats:
    def __init__(self, screen):
        self.screen = screen
        self.active = False
        self.rocket_lives = 0
        self.rocket = None
        self.target = None

    def reset(self):
        self.active = True
        self.rocket_lives = 10
        self.rocket = Rocket(self, self.screen)
        self.target = Target(self, self.screen)

    def update(self):
        if self.rocket_lives == 0:
            self.end()

    def end(self):
        sleep(1)
        self.active = False
