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
