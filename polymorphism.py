class Person:

    def __init__(self, name):
        self.name = name

    def move(self):
        print('Estoy caminando')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('Estoy moviéndome en mi bicicleta')


def main():
    person = Person('Andrés')
    person.move()

    cyclist = Cyclist('Felipe')
    cyclist.move()


if __name__ == '__main__':
    main()
