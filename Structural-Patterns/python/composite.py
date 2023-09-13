# Composite:
# Lets you compose objects into tree structures and then work with these structures as if they were individual objects.

class Component(object):
    "Abstract class"

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):  # Inherits from the abstract class
    "Concrete class"

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # Store name of the composite object
        self.name = args[0]

        # child items
        self.children = []

    def append_child(self, child):

        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        # Print composite object
        print("{}".format(self.name))

        for i in self.children:
            i.component_function()


# Build a composite menu
menu1 = Composite('menu 1')

child1 = Child('child 1')

child2 = Child('child 2')

menu1.append_child(child1)
menu1.append_child(child2)


# composite menu

top = Composite("Top menu")

menu2 = Child('Manue 2')

top.append_child(child1)

top.append_child(child2)


top.component_function()
