#!/usr/bin/python3
"""Define the Rectangle class"""
from base import Base


class Rectangle(Base):
    """
    The rectangle class inherits from the base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the object when called"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self__y = y

    @property
    def width(self):
        """Get the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the value of the width and return an error
        if it does not meet the requirement
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the value of the height and return an error
        if it does not meet the requirement
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of the x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set the value of the x and return an error
        if it does not meet the requirement
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of the x"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set the value of the y and return an error
        if it does not meet the requirement
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__x = value
