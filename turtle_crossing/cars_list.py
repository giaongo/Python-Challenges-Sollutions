from car import Car


class CarsList:

    def __init__(self):
        self.cars_list = []

    def create_car(self):
        car1 = Car()
        self.cars_list.append(car1)
