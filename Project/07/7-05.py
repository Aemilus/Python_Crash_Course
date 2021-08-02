"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

print("Enter 0 to quit.")
active = True
while active:
    age = int(input("What's your age? "))
    if age < 1:
        active = False
    elif age < 3:
        print("Ticket price is free.")
    elif age < 12:
        print("Ticket price is 10$")
    else:
        print("Ticket price is 15$")
