"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
"""

threes = [multiple * 3 for multiple in range(1, 11)]

for three in threes:
    print(three)
