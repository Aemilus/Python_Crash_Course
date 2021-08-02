"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {}

glossary["python"] = "a high level programming language"
glossary["list"] = "a collection that can be iterated"
glossary["tuple"] = "an immutable list"
glossary["variable"] = "a placeholder for values or object reference"
glossary["boolean"] = "a special type of data that can be either False or True"

glossary_term_formatter = "{0}\n\t\t- {1}"

print(glossary_term_formatter.format("python", glossary["python"]))
print(glossary_term_formatter.format("list", glossary["list"]))
print(glossary_term_formatter.format("tuple", glossary["tuple"]))
print(glossary_term_formatter.format("variable", glossary["variable"]))
print(glossary_term_formatter.format("boolean", glossary["boolean"]))
