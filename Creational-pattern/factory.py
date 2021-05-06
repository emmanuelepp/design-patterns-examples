# Factory:
# Provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow"

#### Factory method ####


def get_animal(animal="dog"):

    animals = dict(dog=Dog("Poki"), cat=Cat("Rudy"))

    return animals[animal]


dog = get_animal("dog")

print(dog.speak())

cat = get_animal("cat")

print(cat.speak())
