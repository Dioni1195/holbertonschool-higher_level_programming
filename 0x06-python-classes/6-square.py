#!/usr/bin/python3
class Square:

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    @property
    def position(self):
            return self.__position

    @position.setter
    def position(self, value):
            if type(value) is tuple and len(value) is 2:
                if type(value[0]) is int and type(value[1]) is int:
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, __size=0, __position=(0, 0)):
            self.size = __size
            self.position = __position

    def area(self):
            return self.__size ** 2

    def my_print(self):
            size = self.__size
            pos = self.__position
            if size == 0:
                print()
            else:
                square = [[" "] * pos[0] + ["#"] * size] * size
                new_line = pos[1]
                while new_line > 0:
                    print()
                    new_line -= 1
                for i in square:
                    for j in i:
                        print(j, end="")
                    print()
