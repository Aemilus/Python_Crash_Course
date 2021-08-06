"""
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>> line = "Row, row, row your boat"
>> line.count('row')
2
>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
"""

from utilities import get_file_paths
from utilities import count_the_word

word = "the"

file_paths = get_file_paths()
for filename, filepath in file_paths.items():
    try:
        with open(filepath, encoding="UTF-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print("File %s was not found." % filename)
    else:
        count = count_the_word(contents, word)
        print("The word '%s' appears %d times in file %s." % (word, count, filename))
