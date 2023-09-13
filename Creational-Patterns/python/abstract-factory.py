# Abstract Factory:
# This design pattern lets you produce families of related objects without specifying their concrete classes.

class Dog:

    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"


class DogFactory:
    ### Concrete Factory ###
    def get_pet(self):
        # Returns  a dog object
        return Dog()

    def get_food(self):
        # Returns  a dog food object
        return 'Dog food'


class PetStore:
    def __init__(self, pet_factory=None):
        # pet_factory is our abstract factory

        self._pet_factory = pet_factory

    def show_pet(self):
        # utility method to display the datails

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("it's food is '{}'".format(pet))

        # Create a concrete factory

        factory = DogFactory()

        # Creeate a pet store to our abstract factory

        shop = PetStore(factory)

        # Invoke the utility method to show the details of our pet
        shop.show_pet()
