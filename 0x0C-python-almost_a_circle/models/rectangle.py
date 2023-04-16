#!/usr/bin/python3
'''Module to define a Recatngle'''
from models.base import Base

class Rectangle(Base):
    '''
    This class defines a rectangle
    and inherits from superclass
    Base.
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''Rectangle width'''
        return(self.__width)

    @width.setter
    def width(self, width):
        self.IntegerValidation("width", width, True)
        self.__width = width

    @property
    def height(self):
        '''Rectangle height'''
        return(self.__height)

    @height.setter
    def height(self, height):
        self.IntegerValidation("height", height, True)
        self.__height = height

    @property
    def x(self):
        '''x of rectangle'''
        return(self.__x)

    @x.setter
    def x(self, x):
        self.IntegerValidation("x", x, False)
        self.__x = x

    @property
    def y(self):
        '''y of rectangle'''
        return(self.__y)

    @y.setter
    def y(self, y):
        self.IntegerValidation("y", y, False)
        self.__y = y

    def IntegerValidation(self, name, value, wh=True):
        '''Method to Validate int'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if wh and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not wh and value < 0: 
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Area of rectangle'''
        return self.width * self.height

    def display(self):
        '''displays str rep of rectangle'''

        '''
        for i in range(self.height):
            print('#' * self.width)
        '''
        rect = '\n' * self.y + (' ' * self.x + '#'\
                * self.width + '\n') * self.height
        print(rect, end='')

    def __str__(self):
        return("[{}] ({}) {}/{} - {}/{}".format\
                (type(self).__name__, self.id, self.x, self.y,\
                self.width, self.height))

    def update(self, *args, **kwargs):
        '''updates instances based on args or kwargs'''
        attrs = ('id', 'width', 'height', 'x', 'y')
        if args:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)

        if kwargs:
            for attr, arg in kwargs.items():
                setattr(self, attr, arg)

    def to_dictionary(self):
        return({
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                })
