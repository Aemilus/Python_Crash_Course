"""
12-5. Sideways Shooter: Write a game that places a ship on the left side of the
screen and allows the player to move the ship up and down. Make the ship fire
a bullet that travels right across the screen when the player presses the spacebar.
Make sure bullets are deleted once they disappear off the screen.
"""

import pygame

from game_mechanics import check_events
from rocket import Rocket

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sideways Shooter")
bg_color = (40, 80, 100)
rocket = Rocket(screen)

while True:
    check_events(rocket)
    screen.fill(bg_color)
    rocket.update()
    rocket.update_bullets()
    rocket.blitme()
    rocket.draw_bullets()
    pygame.display.flip()
