"""Prompts for the user’s favorite number and stores this number to a file"""

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


fav = ask_favorite_number()
save_favorite_number(fav)
