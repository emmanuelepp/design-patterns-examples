# Iterator:
# Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc).

def count_names(count):

    names = ['Ana', 'Bob', 'Cathe', 'Emma']

    iterator = zip(range(count), names)

    for position, number in iterator:

        yield number


for num in count_names(3):
    print('{}'.format(num))
