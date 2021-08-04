"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User:
    """Storing a user profile."""
    def __init__(self, first_name, last_name, email, group, password_expired, login_attempts):
        """Build user profile."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.group = group.title()
        self.password_expired = password_expired
        self.login_attempts = login_attempts

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User("laura", "pausini", "laura@company.it", "singers", False, 2)
print("Login attempts for this user:", user_0.login_attempts)

for i in range(4):
    user_0.increment_login_attempts()
else:
    print("Login attempts for this user:", user_0.login_attempts)

user_0.reset_login_attempts()
print("Login attempts for this user:", user_0.login_attempts)
