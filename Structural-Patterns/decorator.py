# Decorator:
# Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

from functools import wraps


def make_blink(function):
    # This amke the decorator transparent in terms of it's name and docstring
    @wraps(function)
    def decorator():

        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function
        return '<blink>' + ret + '</blink>'

    return decorator

# apply your decorator here!


@make_blink
def say_hello():
    """Test"""
    return 'Hi, how are you'


# Check the result of decorator
print(say_hello())

# Check the function
print(say_hello.__name__)

# Check the docstring
print(say_hello.__doc__)
