"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""


def describe_city(city, country="Norway"):
    """Prints in which country a city is."""
    print("{0} is in {1}.".format(city, country))


describe_city("Oslo")
describe_city("Moscow", "Russia")
describe_city(country="Romania", city="Bucharest")
