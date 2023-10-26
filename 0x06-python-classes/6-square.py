#!/usr/bin/python3
''' A class representing a square with a size attribute. '''


class Square:
    ''' Function 'check' verifies whether the value is an integer
    and checks if the value is less than zero. '''
    def check(value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    ''' Function 'check_1' checks if the elements in the tuple
    are two positive integers. '''
    def check_1(tup):
        if len(tup) != 2 or not (isinstance(tup[0], int) and isinstance(tup[1], int)):

            raise TypeError('position must be a tuple of 2 positive integers')
        if tup[0] < 0 or tup[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    ''' Initializes the size and position of the square. '''
    def __init__(self, size=0, position=(0, 0)):
        Square.check(size)
        Square.check_1(position)
        self.__position = position
        self.__size = size

    ''' Computes and returns the area of the square. '''
    def area(self):
        return self.__size ** 2

    ''' Gets the value of the size of the square. '''
    @property
    def size(self):
        return self.__size

    ''' Sets the size of the square. '''
    @size.setter
    def size(self, value):
        Square.check(value)
        self.__size = value

    ''' Returns the tuple position. '''
    @property
    def position(self):
        return self.__position

    ''' Sets the elements inside the position tuple. '''
    @position.setter
    def position(self, value):
        Square.check_1(value)
        index = 0

        for count in value:
            self.__position[index] = count
            index += 1

    ''' Prints the area of the square with '#' symbols. '''
    def my_print(self):
        if self.__size != 0:
            incat = 0
            area = self.area()
            size_1 = self.__size

            for i in range(self.__position[1]):
                print()
            while size_1 <= area:
                counter = 0
                print(" "*self.__position[0], end="")
                while counter < self.__size:
                    incat = 1
                    print("#", end="")
                    counter +=1
                size_1 += self.__size
                print()
        else:
            print()

