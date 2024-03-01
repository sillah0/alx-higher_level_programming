#!/usr/bin/python3
"""import Rectangle class"""


from models.rectangle import Rectangle

"""square class"""


class Square(Rectangle):
    """square class inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing instance atrributes
        Args:
        size (int): size
        x (int): x
        y (int): y
        id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string to be printed"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """get size
        Return: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """set size value
        Args:
            value (int): size
        """
        self.width = value
        self.heignt = value

    def update(self, *args, **kwargs):
        """asigning arguments to each atrri"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)