"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
"""

from collections import OrderedDict

glossary = OrderedDict()

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
