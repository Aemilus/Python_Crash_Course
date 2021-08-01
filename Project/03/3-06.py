"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

guests = ["Simona", "Maria", "Irina"]

print("\nGuests list:\n{0}\n".format(guests))

message = 'Hi {0}! Are you free for Saturday 8pm to have dinner?'

print("Sending invitations:")
print(message.format(guests[0]))
print(message.format(guests[1]))
print(message.format(guests[2]))

not_available = "\n{0} just texted me and she can't make it to dinner.\n"
print(not_available.format(guests[1]))

print("Replacing {0} with someone else.".format(guests[1]))
guests[1] = "Diana"

print("\nGuests list:\n{0}\n".format(guests))

print("Sending new set of invitations:")
print(message.format(guests[0]))
print(message.format(guests[1]))
print(message.format(guests[2]))

print("\nHey, a friend of mine said he has a bigger table available and will borrow it.\n")

print("Expanding list of guests..")
guests.insert(0, "Jimmy")
middle = len(guests) // 2
guests.insert(middle, "Patrick")
guests.append("Mathew")

print("\nGuests list:\n{0}\n".format(guests))

print("Sending new set of invitations:")
for guest in guests:
    print(message.format(guest))

