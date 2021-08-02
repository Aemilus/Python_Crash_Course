"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""

number = int(input("Enter a number: "))

if number % 10 == 0:
    print("It's a multiple of 10.")
else:
    print("It's not a multiple of 10.")
