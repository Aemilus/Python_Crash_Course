"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from admin import Admin

admin_0 = Admin("Keanu", "Reeves", "keanu@continental.gg")
admin_0.privileges.show_privileges()
