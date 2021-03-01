class WashingMachine:

    def __init__(self):
        pass

    def wash(self,  temperature='fría'):
        self.fill_water_tank(temperature)
        self.add_soap()
        self._wash()
        self.spin()

    def fill_water_tank(self, temperature):
        print(f'Llenando el tanque con agua {temperature}')

    def add_soap(self):
        print(f'Añadiendo Jabón')

    def _wash(self):
        print('Lavando la ropa')

    def spin(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    washing_machine = WashingMachine()
    washing_machine.wash()
