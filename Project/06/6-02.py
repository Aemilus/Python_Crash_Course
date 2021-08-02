"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""

favorite_numbers = {
        "john": 6,
        "laura": 23,
        "marius": 5,
        "emil": 8,
        "victor": 10
    }

line_formatter = "{0:<10}:{1:>4}"

print("People's favorite numbers:")
print(line_formatter.format("John", favorite_numbers["john"]))
print(line_formatter.format("Laura", favorite_numbers["laura"]))
print(line_formatter.format("Marius", favorite_numbers["marius"]))
print(line_formatter.format("Emil", favorite_numbers["emil"]))
print(line_formatter.format("Victor", favorite_numbers["victor"]))
