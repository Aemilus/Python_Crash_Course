"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

guests = ["Simona", "Maria", "Irina"]

print("\nGuests list:\n{0}\n".format(guests))

message = 'Hi {0}! Are you free for Saturday 8pm to have dinner?'

print("Sending invitations:")
print(message.format(guests[0]))
print(message.format(guests[1]))
print(message.format(guests[2]))
