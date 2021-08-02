"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""

person = {
        "first_name": "Laura",
        "last_name": "Bobocel",
        "age": 28,
        "city": "Bucharest"
    }

person_info_formatter = "{0:<15}:{1:>15}"

print(person_info_formatter.format("First name", person["first_name"]))
print(person_info_formatter.format("Last name", person["last_name"]))
print(person_info_formatter.format("Age", person["age"]))
print(person_info_formatter.format("City", person["city"]))
