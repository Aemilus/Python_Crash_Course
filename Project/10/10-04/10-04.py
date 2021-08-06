"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = "guest_book.txt"

with open(filename, "w") as file:
    while True:
        name = input("Enter visitor name: ").strip()
        if name == "":
            # exit loop if name is empty string
            break
        else:
            # record visitor name
            print("Welcome visitor %s." % name)
            file.write("Visitor: %s\n" % name)
