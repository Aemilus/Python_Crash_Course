"""
12-2. Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen and match the background color of the image to the background
color of the screen, or vice versa.
"""
import sys

import pygame

from hero import Hero

# init game
pygame.init()
# set screen
screen = pygame.display.set_mode((1000, 600))
# set title
pygame.display.set_caption("The Python Hero")
# background color
bg_color = (0, 150, 255)
# hero object
hero = Hero(screen)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # close event
        if event.type == pygame.QUIT:
            sys.exit()

    # redraw the screen at each loop
    # - set background
    screen.fill(bg_color)
    # - draw hero
    hero.blitme()
    # display screen
    pygame.display.flip()
