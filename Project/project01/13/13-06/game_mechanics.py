import sys

import pygame
from pygame.sprite import groupcollide

from game_elements import Ball


def check_events(catcher):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                catcher.moving_left = True
            elif event.key == pygame.K_RIGHT:
                catcher.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                catcher.moving_left = False
            elif event.key == pygame.K_RIGHT:
                catcher.moving_right = False


def check_ball_group(screen, catcher_group, ball_group):
    # if no ball in the group then make new ball
    if len(ball_group) == 0:
        ball = Ball(screen)
        ball_group.add(ball)

    # if the ball collided with catcher then remove ball
    groupcollide(catcher_group, ball_group, False, True)

    # if the ball in the group dropped pass by the catcher then remove it
    for ball in ball_group.copy():
        if ball.rect.top > screen.get_rect().bottom:
            ball_group.remove(ball)
            # also the player has lost a life
            for catcher in catcher_group.sprites():
                catcher.lives -= 1

