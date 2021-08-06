def city_country(city, country, population=""):
    """Return city, country - population"""
    city = city.title()
    country = country.title()
    city_and_country = "%s, %s" % (city, country)
    if population:
        return "%s - population %s" % (city_and_country, population)
    else:
        return city_and_country
