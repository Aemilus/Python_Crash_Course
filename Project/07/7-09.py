"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""

sandwich_orders = ["cheese", "pastrami", "tuna", "pastrami", "egg", "chicken", "beef", "pastrami", "egg", "beef"]
finished_sandwich = []

print("I need to make following sandwiches:", sandwich_orders)

print("But we've run out of pastrami. I need to remove the orders for pastrami sandwich")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("Remaining sandwich orders:", sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your {0} sandwich.".format(sandwich))
    finished_sandwich.append(sandwich)
else:
    print("Finished making all this sandwiches:", finished_sandwich)
