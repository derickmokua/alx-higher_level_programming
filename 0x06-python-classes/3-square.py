#!/usr/bin/python3
"""Definesnclass Square"""


class Square:
    """
    defines properties of square by: (based on 2-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of a square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the square area.

        Returns: the current square area.
        """
        return self.__size ** 2
