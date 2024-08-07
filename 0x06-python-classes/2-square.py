#!/usr/bin/python3
# square module
"""Module defines a square"""


class Square:
    """A simple class to define a square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size(int): size of square,default value is 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size less than or equals to zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
