"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""


def make_shirt(size="L", text="I love Python"):
    """Makes a T-Shirt of specified size and a text on it."""
    print("Making an {0} size t-shirt with following text on it: '{1}'.".format(size, text))


make_shirt()
make_shirt(size="M")
make_shirt(size="XXL", text="I love Java")
