"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""

print("Type 'q' to quit.")
while True:
    try:
        a = input("Enter first number: ").lower()
        if a == "q":
            break

        b = input("Enter second number: ").lower()
        if b == "q":
            break

        c = int(a) + int(b)
    except ValueError:
        print("This program accepts only integer values.")
    else:
        print("Sum of the two numbers is %d." % c)
