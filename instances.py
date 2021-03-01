class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_coordinate):
        x_diff = (self.x - another_coordinate.x)**2
        y_diff = (self.y - another_coordinate.y)**2

        return (x_diff + y_diff)**0.5


def run():
    coordinate_1 = Coordinate(3, 20)
    coordinate_2 = Coordinate(4, 8)

    print(coordinate_1.distance(coordinate_2))


if __name__ == '__main__':
    run()
