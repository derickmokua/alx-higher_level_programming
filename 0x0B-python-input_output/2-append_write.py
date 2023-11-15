#!/usr/bin/python3
"""Module housing the append_write function."""

def append_write(filename="", text=""):
    """Appends a string to a text file (UTF-8) and returns the number of characters added.

Args:
    filename (str, optional): The name of the file. Defaults to an empty string.
    text (str, optional): The text to append to the file. Defaults to an empty string.

Returns:
    int: The number of characters appended to the file.
"""

    with open(filename, 'a', encoding="utf-8") as f:
        """Returns the count of characters appended to a file by this method."""
        return f.write(text)
