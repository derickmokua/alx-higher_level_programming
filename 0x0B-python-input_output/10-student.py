#!/usr/bin/python3

"""Module defining the class Student based on 9-student.py"""

class Student:
    """
    Class that defines properties of a student.

    Attributes:
        first_name (str): First name of the student.
        last_name (int): Last name of the student.
        age (int): Age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Creates new instances of Student.

        Args:
            first_name (str): First name of the student.
            last_name (int): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved. Otherwise, all attributes must be retrieved.

        Args:
            attrs (list of str, optional): List of attributes to retrieve.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
