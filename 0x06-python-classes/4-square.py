#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Square class."""

    def __init__(self, size=0):
        """Square class initialized"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Gets the data"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the data"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area"""
        return self.__size**2
