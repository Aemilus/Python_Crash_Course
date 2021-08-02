"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""


def city_country(city, country):
    """Returns a string with a city and its country."""
    return "{0}, {1}".format(city.title(), country.title())


print(city_country("Bucharest", "Romania"))
print(city_country("santiago", "CHILE"))
print(city_country(country="india", city="Delhi"))
