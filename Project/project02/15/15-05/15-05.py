"""
15-5. Refactoring: The fill_walk() method is lengthy. Create a new method
called get_step() to determine the direction and distance for each step, and
then calculate the step. You should end up with two calls to get_step() in
fill_walk():
x_step = self.get_step()
y_step = self.get_step()
This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.
"""