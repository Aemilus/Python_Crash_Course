"""
2-9. Favorite Number: Store your favorite number in a variable. Then, using
that variable, create a message that reveals your favorite number. Print that
message.
"""

# solution 1
number = 2
message = "My favorite number is " + str(number) + "."
print(message)

# solution 2
print("My favorite number is %d." % number)
