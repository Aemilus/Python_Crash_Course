"""
13-5. Catch: Create a game that places a character that you can move left and
right at the bottom of the screen. Make a ball appear at a random position at
the top of the screen and fall down the screen at a steady rate. If your character
“catches” the ball by colliding with it, make the ball disappear. Make a new
ball each time your character catches the ball or whenever the ball disappears
off the bottom of the screen.
"""

import pygame
from pygame.sprite import Group

from game_elements import Catcher
from game_mechanics import check_events
from game_mechanics import check_ball_group

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Catch")
bg_color = (70, 150, 200)

catcher = Catcher(screen)
catcher_group = Group()
catcher_group.add(catcher)

ball_group = Group()

while True:
    check_events(catcher)
    screen.fill(bg_color)

    check_ball_group(screen, catcher_group, ball_group)

    catcher_group.update()
    ball_group.update()

    catcher_group.draw(screen)
    ball_group.draw(screen)

    pygame.display.flip()
