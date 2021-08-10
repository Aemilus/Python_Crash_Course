import sys

import pygame
from pygame.sprite import spritecollideany


def check_events(game, play_button, rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not game.active:
                game.reset()


def check_keydown_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_SPACE:
        rocket.fire_bullet()


def check_keyup_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_collisions(bullets, target):
    bullet_collided = spritecollideany(target, bullets)
    if bullet_collided is not None:
        bullets.remove(bullet_collided)
