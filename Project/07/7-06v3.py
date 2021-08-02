"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

print("Enter 0 to quit.")
while True:
    age = int(input("What's your age? "))
    if age < 0:
        continue
    elif age == 0:
        break
    elif age < 3:
        print("Ticket price is free.")
    elif age < 12:
        print("Ticket price is 10$")
    else:
        print("Ticket price is 15$")
