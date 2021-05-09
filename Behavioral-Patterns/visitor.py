# Visitor:
# Lets you separate algorithms from the objects on which they operate.
class House(object):  # Class visited
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_tv(self, tv_specialist):
        print(self, 'worked on by ', tv_specialist)

    def work_on_electricity(self, eletrician):
        print(self, 'worked on by ', eletrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    # abstract visitor
    def __str__(self):
        return self.__class__.__name__


class TvSpecialist(Visitor):
    # Concrete visitor
    def visit(self, house):
        house.work_on_tv(self)


class Electrician(Visitor):
    # Concrete visitor
    def visit(self, house):
        house.work_on_electricity(self)


# Create a tv visitor
tvv = TvSpecialist()

# Create a electrician visitor
elec = Electrician()
# Create  house
home = House()

# Accept a tv spacialist visitor
home.accept(tvv)
# Accept a electrician visitor
home.accept(elec)
