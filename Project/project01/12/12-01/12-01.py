"""
12-1. Blue Sky: Make a Pygame window with a blue background.
"""

import sys
import pygame

# tuple with rgb for blue color
blue_rgb = (0, 150, 255)

# init game
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Blue Background")

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # close event
            sys.exit()
    # fill screen background
    screen.fill(blue_rgb)
    # display screen
    pygame.display.flip()
