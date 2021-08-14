from random import randint


class Die:
    def __init__(self, sides_count=6):
        self.sides_count = sides_count

    def roll(self):
        return randint(1, self.sides_count)
