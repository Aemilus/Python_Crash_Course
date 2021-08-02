"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""


def make_shirt(size, text):
    """Makes a T-Shirt of specified size and a text on it."""
    print("Making an {0} size t-shirt with following text on it: '{1}'.".format(size, text))


make_shirt("XXL", "Python apprentice")
make_shirt(text="What's up?", size="L")
