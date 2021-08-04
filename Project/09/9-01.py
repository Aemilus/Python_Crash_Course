"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""


class Restaurant:
    """A class for making a restaurant with a specific cuisine."""
    def __init__(self, restaurant_name, cuisine_type):
        """Constructor of Restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()

    def describe_restaurant(self):
        """Print attributes of Restaurant."""
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        """Print a dummy message to say the restaurant is open."""
        print(self.restaurant_name, "is now open.")


restaurant = Restaurant("The Boat", "lebanese")

print("Printing the attributes of restaurant instance individually..")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\nCalling the methods of class Restaurant..")
restaurant.describe_restaurant()
restaurant.open_restaurant()
