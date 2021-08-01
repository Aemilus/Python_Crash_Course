"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""

usernames = ["bob", "john", "admin", "guest", "diana", "paula"]

usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello {0}, would you like to see the health-check logs for today?".format(user))
        else:
            print("Hello {0}, how are you today?".format(user))
else:
    print("We need to find some users!")
