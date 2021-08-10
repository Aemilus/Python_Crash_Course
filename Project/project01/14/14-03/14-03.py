"""
14-3. Challenging Target Practice: Start with your work from Exercise 14-2
(page 298). Make the target move faster as the game progresses, and restart
at the original speed when the player clicks Play.
"""

import pygame

from game_elements import GameStats
from game_elements import Button
from game_mechanics import check_events
from game_mechanics import check_collisions

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Challenging Target Practice")
bg_color = (180, 160, 140)

game = GameStats(screen)

play_button = Button(screen, "Play")

while True:
    screen.fill(bg_color)
    check_events(game, play_button, game.rocket)
    if game.active:
        check_collisions(game.rocket.bullets, game.target)

        game.rocket.update()
        game.rocket.draw_rocket()

        game.target.update()
        game.target.draw_target()

        game.rocket.bullets.update_bullets()
        game.rocket.bullets.draw_bullets()

        game.update()
    else:
        play_button.draw_button()

    pygame.display.flip()
