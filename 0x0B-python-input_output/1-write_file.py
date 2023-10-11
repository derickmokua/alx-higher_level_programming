#!/usr/bin/python3
"""Module for function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written.

Args:
    filename (str, optional): The name of the file. Defaults to an empty string.
    text (str, optional): The text to write to the file. Defaults to an empty string.

Returns:
    int: The number of characters written to the file.
"""

    with open(filename, 'w', encoding="utf-8") as f:
        """Returns the count of characters written to a file by this method."""
        return f.write(text)
