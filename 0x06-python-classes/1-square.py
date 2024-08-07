#!/usr/bin/python3
# modules defines a square
""" This module defines a square"""


class Square:
    """ A simple class to describe a square """

    def __init__(self, size) -> None:
        """Initializing square properties

        Args: size (int): Size of a square
        """
        self.__size = size
