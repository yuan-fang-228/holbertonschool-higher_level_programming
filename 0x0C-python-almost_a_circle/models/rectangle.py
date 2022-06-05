#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """return dictionary representation of the rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        if args is not None and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for argument in kwargs:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "width" in kwargs:
                    self.width = kwargs["width"]
                if "height" in kwargs:
                    self.height = kwargs["height"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def checkInt(self, value, attributeName):
        """check whether the attribute is integer or not"""
        if type(value) is not int:
            raise TypeError(f"{attributeName} must be an integer")
        if attributeName == "width" or attributeName == "height":
            if value <= 0:
                raise ValueError(f"{attributeName} must be > 0")
        if attributeName == "x" or attributeName == "y":
            if value < 0:
                raise ValueError(f"{attributeName} must be >= 0")

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width value"""
        self.checkInt(value, "width")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height value"""
        self.checkInt(value, "height")
        self.__height = value

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x value"""
        self.checkInt(value, "x")
        self.__x = value

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y value"""
        self.checkInt(value, "y")
        self.__y = value

    def area(self):
        """return the area of the rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """print in stdout Rectangle with character #"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """return the formatted string when printing"""
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"
