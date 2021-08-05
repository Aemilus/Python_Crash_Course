"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

from users import Admin

admin_0 = Admin("Keanu", "Reeves", "keanu@continental.gg")
admin_0.privileges.show_privileges()
