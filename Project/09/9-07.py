"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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


class Admin(User):
    """Dedicated for administrator user profiles."""
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email, group="admins", password_expired=False, login_attempts=0)
        self.privileges = ["can add post", "can delete post", "can ban user", "can reset passwords", "can create users"]

    def show_privileges(self):
        print("Privileges:", self.privileges)


admin = Admin("antonio", "banderas","antonio@admins.it")
admin.describe_user()
admin.greet_user()
admin.show_privileges()
