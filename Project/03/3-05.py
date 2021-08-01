"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
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
