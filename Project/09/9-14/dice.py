"""Module for Dice class."""

from random import randint


class Dice:
    """Dice class."""
    def __init__(self, sides=6):
        self.sides = sides
        print("Created a %s-sided dice." % self.sides)

    def roll_dice(self):
        print("The dice has", self.sides, "sides.")
        print("Dice roll:", randint(1, self.sides))
