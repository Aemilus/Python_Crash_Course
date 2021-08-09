"""
13-2. Better Stars: You can make a more realistic star pattern by introducing
randomness when you place each star. Recall that you can get a random number
like this:
from random import randint
random_number = randint(-10,10)
This code returns a random integer between −10 and 10. Using your code
in Exercise 13-1, adjust each star’s position by a random amount.
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
