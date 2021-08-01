"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""

foods = ("scrambled eggs", "bread", "sparkling water", "coca cola", "pancake")

print("We offer below foods:")
for food in foods:
    print(food)

try:
    print("\nTrying to replace first food in the menu..")
    foods[0] = "fried chicken"
except Exception as ex:
    print("You can't do changes in the menu because", ex)

print("\nReplacing the entire menu..")
foods = ("fried chicken", "bread", "tea", "coca cola", "pancake")

print("We now offer:")
for food in foods:
    print(food)
