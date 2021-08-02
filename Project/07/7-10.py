"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

print("Start poll.")
dream_vacations = {}

active = True
while active:
    answer = input("Would you like to participate in our Dream Vacation poll? Please enter 'yes' or 'no': ").lower()
    if answer == "yes":
        name = input("Please enter your name: ")
        place = input("Please enter what's your dream vacation place: ")
        dream_vacations[name] = place
    else:
        active = False
else:
    print("Poll stop.")

print("Poll results.")
for name, place in dream_vacations.items():
    print("{0:15}: {1:>15}".format(name, place))
