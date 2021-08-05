"""Module for Privileges and Admin classes."""

from user import User


class Privileges:
    """Stores the privileges of Admin users."""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can reset passwords", "can create users"]

    def show_privileges(self):
        print("Privileges:", self.privileges)


class Admin(User):
    """Dedicated for administrator user profiles."""
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email, group="admins", password_expired=False, login_attempts=0)
        self.privileges = Privileges()
