"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

favorite_numbers = {
        "john": [6, 8, 20],
        "laura": [23, 4, 10],
        "marius": [5],
        "emil": [8, 0],
        "victor": [10, 100, 1000, 10000]
    }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t- " + str(number))
    else:
        print()
