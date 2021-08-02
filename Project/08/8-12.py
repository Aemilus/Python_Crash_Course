"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
"""


def add_ingredients(*ingredients):
    if ingredients:
        print("The sandwich will be made with following ingredients:")
        for ingredient in ingredients:
            print("\t- {0}".format(ingredient.lower()))


add_ingredients("onion", "tomatoes", "cheese")
add_ingredients("cucumber", "garlic", "mayo", "avocado")
add_ingredients()
