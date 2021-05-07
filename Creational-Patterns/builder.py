# Builder:
# This pattern let you construct complex objects step by step.

class Director():
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    # abstract builder
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class CarBuilder(Builder):
    # Concrete builder ---> privide parts
    def add_model(self):
        self.car.model = 'Rav4'

    def add_tires(self):
        self.car.tires = 'Winter tires'

    def add_engine(self):
        self.car.engine = 'V6'


class Car():
    # Product
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f'{self.model},|{self.tires},|{self.engine}'


builder = CarBuilder()

director = Director(builder)

director.construct_car

car = director.get_car()

print(car)
