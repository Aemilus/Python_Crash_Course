import unittest

from Employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """TestCase for Employee class."""

    def setUp(self) -> None:
        self.employee = Employee("laura", "popesCU", "120000")

    def test_give_default_raise(self):
        expected_annual_salary = 125000
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, expected_annual_salary)

    def test_give_custom_raise(self):
        expected_annual_salary = 140000
        self.employee.give_raise("20000")
        self.assertEqual(self.employee.annual_salary, expected_annual_salary)


if __name__ == '__main__':
    unittest.main()
