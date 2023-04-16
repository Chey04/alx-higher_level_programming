#!/usr/bin/python3
'''Defines a Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        '''Constuctor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String rep of square'''
        return ("[{}] ({}) {}/{} - {}".format(\
                type(self).__name__, self.id, self.x, self.y,\
                self.width))

    @property
    def size(self):
        '''size of square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates values either through args or kwargs'''
        attrs = ('id', 'size', 'x', 'y')
        if args:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        elif kwargs:
            for attr, arg in kwargs.items():
                setattr(self, attr, arg)

    def to_dictionary(self):
        '''dict representation of square'''
        return {'id': self.id, 'size': self.size, 'x': self.x,\
                'y': self.y}
