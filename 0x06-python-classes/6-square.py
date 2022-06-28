#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Square class initialized"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            val = self.__position[0]
            if val > 0:
                print(' ' * val, end='')
            for j in range(self.__size):
                print('#', end='')
            print()
