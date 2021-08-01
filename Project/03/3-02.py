"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.
"""

names = ["John", "Larisa", "Andreea", "Michael", "Victor", "George"]

message = "Hello {0}! How are you today?"

print(message.format(names[0]))
print(message.format(names[1]))
print(message.format(names[2]))
print(message.format(names[3]))
print(message.format(names[4]))
print(message.format(names[5]))
