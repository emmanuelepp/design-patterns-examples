# Observer:
# Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

class Subject(object):  # <----- observed
    def __init__(self):
        self._observers = []

    def attach(self, observer):  # <------- Append observer if the list has not been  observed
        if observer not in self._observers:

            self._observers.append(observer)

    def detach(self, observer):  # <----- remove observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):  # <----- Alert the observers

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp


class TempViewer:

    def update(self, subject):
        print('Temp viewer: {} as temp {}'.format(subject._name, subject._temp))


A1 = Core("A1")
A2 = Core("A2")

##########

B1 = TempViewer()
B2 = TempViewer()

##########

A1.attach(B1)
A1.attach(B2)

##########

A1.temp = 70
A1.temp = 100
