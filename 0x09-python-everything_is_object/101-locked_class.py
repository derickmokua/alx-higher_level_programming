#!/usr/bin/python3
"""Describes a LockedClass class"""

class LockedClass:
    """
    Restricts dynamic creation of new instance attributes, except for the 'inclu     de_name' attribute.

    Attributes:
        first_name (str): The first name of something.

    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Instantiates new objects of the LockedClass."""

        self.first_name = "first_name"
