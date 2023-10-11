#!/usr/bin/python3
"""This module defines a function to generate Pascal's Triangle."""

def pascal_triangle(n):
	"""Generate Pascal's Triangle up to the nth row.

	Args:
    	n (int): The number of rows in Pascal's Triangle.

	Returns:
    	list of lists of integers: A representation of Pascal's Triangle with 'n' rows.
	"""

	if n <= 0:
		return []
	if n == 1:
		return [[1]]

	pascal = [[1]]
	for i in range(n - 1):
		pascal.append([x + n for x, n in zip(pascal[-1] + [0],[0] + pascal[-1])])
	return (pascal)
