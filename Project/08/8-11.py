"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
    return magicians


print("This is a list of magicians:")
dark_magicians = ["Magician of Black Chaos", "Dark Magician", "Dark Magician Girl", "Magician's Rod"]
show_magicians(dark_magicians)

print("\nMaking the magicians greater..")
great_magicians = make_great(dark_magicians[:])

print("\nOriginal list of magicians:")
show_magicians(dark_magicians)
print("\nThe list with great magicians:")
show_magicians(great_magicians)
