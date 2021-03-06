"""
9-14. Dice: The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from dice import Dice


def roll_dice_several_times(dice, times=10):
    print("Roll the dice for %s times." % times)
    for i in range(times):
        dice.roll_dice()


six_sided_dice = Dice()
roll_dice_several_times(six_sided_dice)

ten_sided_dice = Dice(10)
roll_dice_several_times(ten_sided_dice)

twenty_sided_dice = Dice(20)
roll_dice_several_times(twenty_sided_dice)
