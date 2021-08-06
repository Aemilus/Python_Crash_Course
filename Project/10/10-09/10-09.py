"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

cats_filename = "cats.txt"
dogs_filename = "dogs.txt"

for filename in [cats_filename, dogs_filename]:
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print("Contents of %s file:" % filename)
        print(contents.rstrip())
