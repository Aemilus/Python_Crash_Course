"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
"""

guests = ["Simona", "Maria", "Irina"]

print("\nGuests list:\n{0}\n".format(guests))

message = 'Hi {0}! Are you free for Saturday 8pm to have dinner?'

print("Sending invitations:")
print(message.format(guests[0]))
print(message.format(guests[1]))
print(message.format(guests[2]))

number_of_invitations = len(guests)
print("\nI've sent {0} invitations.\n".format(number_of_invitations))
