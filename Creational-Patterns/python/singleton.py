class Acron:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Acron):
    # This class share all attributes in the other instances

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the atribute in the dictionary
        self._shared_state.update(kwargs)

    def __str__(self):
        # return the dictionry
        return str(self._shared_state)


acronym1 = Singleton(DNS="Domain Name System")
print(acronym1)

acronym2 = Singleton(SMTP="Simple Mail Transfer Protocol")
print(acronym2)
