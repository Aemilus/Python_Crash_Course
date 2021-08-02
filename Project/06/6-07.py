"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person_0 = {
        "first_name": "Laura",
        "last_name": "Bobocel",
        "age": 28,
        "city": "Bucharest"
    }

person_1 = {
        "first_name": "John",
        "last_name": "Robinson",
        "age": 60,
        "city": "London"
    }

person_2 = {
        "first_name": "Matilde",
        "last_name": "Bovary",
        "age": 38,
        "city": "Paris"
    }

people = [person_0, person_1, person_2]

for person in people:
    print("Person details:")
    line_formatter = "{0:25}:{1:>15}"
    for info, value in person.items():
        print(line_formatter.format(info.replace("_", " ").title(), value))
    else:
        print()
