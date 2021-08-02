"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

cities = {
    "bucharest": {
        "country": "Romania",
        "population": 2_000_000,
        "fact": "The traffic is terrible."
    },
    "berlin": {
        "country": "Germany",
        "population": 4_000_000,
        "fact": "The city has an oceanic climate."
    },
    "paris": {
        "country": "France",
        "population": 3_000_000,
        "fact": "Many artists have made this city their home."
    }
}

for city, city_dict in cities.items():
    print("Some things you should know about {0}:".format(city.title()))
    for city_k, city_v in city_dict.items():
        print("\t{0:15}: {1:^15}".format(city_k.title(), city_v))
    else:
        print()
