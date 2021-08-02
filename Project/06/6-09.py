"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
"""

favorite_places = {
    "laura": ["sinaia", "sibiu", "busteni", "brasov", "rasnov"],
    "emil": ["svalbard", "caerphilly", "margam"],
    "michael": ["santorini", "black sea", "prague"]
}

for name, places in favorite_places.items():
    print("{0}'s favorite places are:".format(name.title()))
    for place in places:
        print("\t- " + place.title())
    else:
        print()
