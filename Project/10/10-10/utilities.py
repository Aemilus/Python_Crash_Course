"""
Module with needed functions.
"""


def get_file_paths():
    """
    Returns a dictionary where:

    - key:      is the filename with extension
    - value:    is the relative path to the file
    """
    # putting also some files that don't exist
    filenames = ["65991-0", "error", "65995-0", "65998-0", "random_file"]
    file_extension = ".txt"
    relative_path = "./files/"

    file_paths = {}
    for filename in filenames:
        file_paths[filename + file_extension] = relative_path + filename + file_extension

    return file_paths


def count_the_word(text: str, word: str):
    """
    Counts number of appearances for 'word' in the 'text'.
    It is not case sensitive."""
    return text.lower().count(word)

