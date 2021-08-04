"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""


class User:
    """Storing a user profile."""
    def __init__(self, first_name, last_name, email, group, password_expired):
        """Build user profile."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.group = group.title()
        self.password_expired = password_expired

    def describe_user(self):
        """Show user profile."""
        line = "{0:20}: {1:>15}"
        for k, v in self.__dict__.items():
            print(line.format(k, str(v)))

    def greet_user(self):
        """Show a message to the user."""
        if self.password_expired:
            print("Hi", self.first_name, self.last_name, "your password has expired.")
        else:
            print("Hi", self.first_name, self.last_name, "how are you today?")


user_0 = User("laura", "pausini", "laura@company.it", "singers", False)
user_1 = User("emil", "popescu", "emil@gmail.ro", "engineers", True)
user_2 = User("simona", "popovici", "simona@tv.com", "singers", True)
user_3 = User("radu", "georgescu", "radu@admin.com", "admins", False)

users = [user_0, user_1, user_2, user_3]

for user in users:
    user.greet_user()
    user.describe_user()
    print()
