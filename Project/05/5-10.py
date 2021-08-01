"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
"""

current_users = ["bob", "john", "admin", "guest", "diana", "paula"]

new_users = ["John", "Irina", "pauLA", "ADMIN", "GEorGE"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Username {0} is already used. Please enter a new username.".format(new_user))
    else:
        print("Username {0} is available.".format(new_user))
