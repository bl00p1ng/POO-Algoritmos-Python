class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    rectangle = Rectangle(width=3, height=4)
    print(rectangle.area())

    square = Square(side=5)
    print(square.area())
