#!/usr/bin/python3

class MyInt(int):
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, MyInt):
            return self.value != other.value
        return False

    def __ne__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, MyInt):
            return self.value == other.value
    return True
