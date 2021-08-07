"""
Module with functions for handling user actions from keyboard.
"""

import sys

import pygame


def check_events(rocket):
    """Respond to keyboard actions."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def check_keydown_events(event, rocket):
    """Respond to key presses."""
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_SPACE:
        rocket.fire_bullet()


def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False
