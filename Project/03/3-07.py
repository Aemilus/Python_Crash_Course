"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

print("\nBad luck guys, my friend can't bring the new table in time and now I only have two spots available for dinner.")

print("\nCancelling invitations until two people are left on the list..")
while len(guests) > 2:
    guest = guests.pop()
    print("Hi {0}, I need to cancel the earlier invitation. Sorry but there's no more space for you at dinner table.".format(guest))

print("\nGuests list:\n{0}\n".format(guests))

print("Send confirmation to people left on the list that they are still invited..")

for guest in guests:
    print("Hi {0}, this is just to confirm that you are still invited for dinner.".format(guest))

print("\nIt's done. Emptying the list.")
del guests[1]
guests.remove("Jimmy")

print("\nChecking if the list is empty..")
print("\nGuests list:\n{0}\n".format(guests))
