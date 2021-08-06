"""Read number from favorite_number.txt with json load and print the value."""

import json


def load_favorite_number():
    """Return number from a file with json load."""
    try:
        filename = "favorite_number.txt"
        with open(filename) as file:
            number = json.load(file)
            number = int(number)
    except (ValueError, FileNotFoundError):
        return None
    else:
        return number


def print_favorite_number(number: int):
    try:
        print("I know your favorite number! It's %d." % number)
    except (TypeError, ValueError):
        pass


fav = load_favorite_number()
print_favorite_number(fav)
