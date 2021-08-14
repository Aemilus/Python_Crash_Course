from random import choice
from random import randint


class RandomWalk:
    def __init__(self, points_count=5_000):
        # length of walk
        self.points_count = points_count
        # walk starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # keep taking steps until the walk reaches desired length
        while len(self.x_values) < self.points_count:
            # decide which direction to go and how far to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()
            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    @staticmethod
    def get_step():
        direction = choice((-1, 1))
        distance = randint(0, 10)
        step = direction * distance
        return step
