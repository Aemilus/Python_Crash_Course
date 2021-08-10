"""
14-2. Target Practice: Create a rectangle at the right edge of the screen that
moves up and down at a steady rate. Then have a ship appear on the left
side of the screen that the player can move up and down while firing bullets
at the moving, rectangular target. Add a Play button that starts the game, and
when the player misses the target three times, end the game and make the Play
button reappear. Let the player restart the game with this Play button.
"""

import pygame

from game_elements import GameStats
from game_elements import Button
from game_mechanics import check_events
from game_mechanics import check_collisions

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Target Practice")
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
