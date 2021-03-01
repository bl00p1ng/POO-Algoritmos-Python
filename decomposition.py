class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'at_rest'
        self._engine = Engine(cylinders=4)

    def speed_up(self, speed='slow'):
        if speed == 'fast':
            self._engine.injects_gasoline(10)
        else:
            self._engine.injects_gasoline(3)

        self._status = 'on_the_move'


class Engine:
    def __init__(self, cylinders, engine_type='gasoline'):
        self.cylinders = cylinders
        self.type = engine_type
        self.temperature = 0

    def injects_gasoline(self, quantity):
        pass


def run():
    pass


if __name__ == '__main__':
    run()
