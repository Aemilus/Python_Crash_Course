"""
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]


print("This is a list of magicians:")
dark_magicians = ["Magician of Black Chaos", "Dark Magician", "Dark Magician Girl", "Magician's Rod"]
show_magicians(dark_magicians)

print("\nMaking the magicians greater..")
make_great(dark_magicians)
show_magicians(dark_magicians)
