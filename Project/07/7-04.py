"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""

order = True

print("Type 'quit when done.")
while order:
    topping = input("Please enter a pizza topping: ").lower()
    if topping == "quit":
        order = False
    else:
        print("We will add {0} topping to your pizza.".format(topping))
