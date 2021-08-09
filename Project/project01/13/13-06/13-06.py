"""
13-6. Game Over: Using your code from Exercise 13-5 (page 284), keep track
of the number of times the player misses the ball. When they’ve missed the ball
three times, end the game.
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

    if catcher.lives > 0:
        check_ball_group(screen, catcher_group, ball_group)

        catcher_group.update()
        ball_group.update()

        catcher_group.draw(screen)
        ball_group.draw(screen)
    else:
        print("GAME OVER")

    pygame.display.flip()
