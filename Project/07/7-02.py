"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
"""

group_size = abs(int(input("How many people are in the dinner group?\n")))

if group_size > 8:
    print("Sorry, you'll have to wait until we get you a table ready.")
else:
    print("Your table is ready.")
