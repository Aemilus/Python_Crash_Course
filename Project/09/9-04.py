"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
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


restaurant = Restaurant("The Boat", "lebanese")
print("This restaurant has served:", restaurant.number_served)
restaurant.number_served = 10
print("This restaurant has served:", restaurant.number_served)
restaurant.set_number_served(5)
print("This restaurant has served:", restaurant.number_served)
restaurant.increment_number_served(4)
print("This restaurant has served:", restaurant.number_served)
