"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

import json


def ask_favorite_number():
    """Get a favorite number form user input."""
    while True:
        try:
            number = input("What's your favorite number?\n")
            number = int(number)
        except ValueError:
            pass
        else:
            break

    return number


def save_favorite_number(number: int):
    """Store the number in a text file with json dump."""
    filename = "favorite_number.txt"
    with open(filename, "w") as file:
        json.dump(number, file)
    print("Favorite number saved.")


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


def favorite_number():
    """Prints favorite number if stored in file, else get number from user input and save it."""
    number = load_favorite_number()
    if not number:
        number = ask_favorite_number()
        save_favorite_number(number)
    else:
        print_favorite_number(number)


favorite_number()
