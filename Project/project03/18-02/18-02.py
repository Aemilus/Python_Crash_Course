"""
18-2. Short Entries: The __str__() method in the Entry model currently appends
an ellipsis to every instance of Entry when Django shows it in the admin site
or the shell. Add an if statement to the __str__() method that adds an ellipsis
only if the entry is longer than 50 characters. Use the admin site to add an
entry that’s fewer than 50 characters in length, and check that it doesn’t have
an ellipsis when viewed.
"""

# done (see models.py)
