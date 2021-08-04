"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""


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


class IceCreamStand(Restaurant):
    """An ice cream stand can be seen as a specific kind of Restaurant."""

    def __init__(self, stand_name):
        """IceCreamStand constructor"""
        super().__init__(stand_name, cuisine_type="frozen desserts")
        self.flavors = ["vanilla", "chocolate", "lemon", "watermelon", "caramel"]

    def show_flavors(self):
        print("We offer following flavors:", self.flavors)


stand_0 = IceCreamStand("The Frozen Rose")
stand_0.describe_restaurant()
stand_0.open_restaurant()
stand_0.show_flavors()
