"""Module for User class."""


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
