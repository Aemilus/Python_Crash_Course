"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""

favorite_fruits = ["nectarines", "mangoes", "bananas", "apples", "cherry", "pears", "oranges", "limes", "kiwifruit"]

message = "You like {0} very much!"

fruit1 = "apples"
fruit2 = "bananas"
fruit3 = "peaches"
fruit4 = "oranges"
fruit5 = "strawberries"

if fruit1 in favorite_fruits:
    print(message.format(fruit1))
if fruit2 in favorite_fruits:
    print(message.format(fruit2))
if fruit3 in favorite_fruits:
    print(message.format(fruit3))
if fruit4 in favorite_fruits:
    print(message.format(fruit4))
if fruit5 in favorite_fruits:
    print(message.format(fruit5))
