# Adapter:
# Allows objects with incompatible interfaces to collaborate.

class English:

    def __init__(self):
        self.name = 'English'

    def speak_english(self):
        return 'Hi'


class French:

    def __init__(self):
        self.name = 'French'

    def speak_french(self):

        return 'Oui'


class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object

        # Add new dictionary item
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


# List of speakers
objects = []

# Create English object
english = English()
# Create French object
french = French()
# Append the objects to the list

objects.append(Adapter(english, speak=english.speak_english))
objects.append(Adapter(french, speak=french.speak_french))

for obj in objects:
    print("'{}' says '{}' \n".format(obj.name, obj.speak()))
