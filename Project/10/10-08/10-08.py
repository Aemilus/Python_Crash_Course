"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

cats_filename = "cats.txt"
dogs_filename = "dogs.txt"

for filename in [cats_filename, dogs_filename]:
    try:
        with open(filename) as file:
            contents = file.read()
        print("Contents of %s file:" % filename)
        print(contents.rstrip())
    except FileNotFoundError:
        print("File %s is missing." % filename)
