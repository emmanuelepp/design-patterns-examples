import copy
# Prototype
# Let you copy existing objects without making your code dependent on their classes.


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_obj(self, name, obj):
        self._objects[name] = obj

    def unregister_obj(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        # Clone a register object and update the attributes
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)

        return obj


class Car:
    def __init__(self):
        self.name = 'Rav4'
        self.color = 'Blue'
        self.options = 'EX-V6'

    def __str__(self):
        return f'{self.name}, {self.color}, {self.options}'


car = Car()

prototype = Prototype()

prototype.register_obj('Rav4', car)

car1 = prototype.clone('Rav4')

print(car1)
