#!/usr/bin/python3
"""Method for creating a new student instance."""

def append_after(filename="", search_string="", new_string=""):
	"""Inserts 'new_string' into 'filename' after lines containing 'search_string'.
	Args: filename (str, optional): File name. Defaults to "".
	search_string (str, optional): String to search. Defaults to "".
	new_string (str, optional): String to append. Defaults to "".
	"""
	with open(filename, "r") as f:
		text = f.readlines()

	with open(filename, "w") as fo:
		s = ""
	for line in text:
		s += line
		if search_string in line:
			s += new_string
		fo.write(s)

