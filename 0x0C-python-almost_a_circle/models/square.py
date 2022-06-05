#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represent a square class that inheritant from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square class instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return the formatted string of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size value as width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of the instance"""
        if args is not None and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for argument in kwargs:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """return the dictionary representation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
