"""Restaurant module"""


class Restaurant:
    """A class for making a restaurant with a specific cuisine."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Constructor of Restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.lower()
        self.number_served = number_served

    def describe_restaurant(self):
        """Print attributes of Restaurant."""
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        """Print a dummy message to say the restaurant is open."""
        print(self.restaurant_name, "is now open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
