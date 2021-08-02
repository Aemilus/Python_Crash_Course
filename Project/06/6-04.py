"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {}

glossary["python"] = "a high level programming language"
glossary["list"] = "a collection that can be iterated"
glossary["tuple"] = "an immutable list"
glossary["variable"] = "a placeholder for values or object reference"
glossary["boolean"] = "a special type of data that can be either False or True"
glossary["dict"] = "a collection of (key, value) pairs"
glossary["set"] = "a collection of unique elements"

glossary_term_formatter = "{0}\n\t\t- {1}"

for term, meaning in glossary.items():
    print(glossary_term_formatter.format(term, meaning))
