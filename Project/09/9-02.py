"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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


restaurant_0 = Restaurant("The Boat", "lebanese")
restaurant_1 = Restaurant("One million dollars", "mixed")
restaurant_2 = Restaurant("at the crossroads", "romanian")

restaurants = [restaurant_0, restaurant_1, restaurant_2]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    print()
