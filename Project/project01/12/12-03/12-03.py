"""
12-3. Rocket: Make a game that begins with a rocket in the center of the
screen. Allow the player to move the rocket up, down, left, or right using the
four arrow keys. Make sure the rocket never moves beyond any edge of the
screen.
"""

import pygame

from game_mechanics import check_events
from rocket import Rocket

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Rocket")

rocket = Rocket(screen)

while True:
    check_events(rocket)
    screen.fill((255, 150, 0))
    rocket.update()
    rocket.blitme()
    pygame.display.flip()
