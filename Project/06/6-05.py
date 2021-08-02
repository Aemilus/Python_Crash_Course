"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
        "nile": "egypt",
        "danube": "romania",
        "yangtze": "china",
        "ganges": "india"
    }

for river, country in rivers.items():
    river = river.title()
    country = country.title()
    print("The {0} runs through {1}.".format(river, country))

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())
