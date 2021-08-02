"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""

sandwich_orders = ["cheese", "tuna", "egg", "chicken", "beef", "pastrami", "egg", "beef"]
finished_sandwich = []

print("I need to make following sandwiches:", sandwich_orders)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your {0} sandwich.".format(sandwich))
    finished_sandwich.append(sandwich)
else:
    print("Finished making all this sandwiches:", finished_sandwich)
