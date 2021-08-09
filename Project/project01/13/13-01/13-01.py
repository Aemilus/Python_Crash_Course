"""
13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen.
"""

import sys

import pygame

from stars import Stars

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Stars")

stars = Stars(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    stars.draw(screen)

    pygame.display.flip()
