#!/usr/bin/python3
"""Module housing the read_file function."""

def read_file(filename=""):
	"""Reads a file and prints its contents to stdout.

	Args:
	filename (str, optional): The name of the file to read. Defaults to an empty string.
	"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
