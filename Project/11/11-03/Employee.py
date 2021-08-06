class Employee:
    """A class with attributes for an employee."""

    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.annual_salary = int(annual_salary)

    def give_raise(self, amount=5000):
        """Increases annual_salary with an amount. Default is 5000$."""
        self.annual_salary += int(amount)
