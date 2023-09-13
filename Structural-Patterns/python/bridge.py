# Bridge:
# Lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

class DrawApi(object):
    def draw_circle(self, x, y, radius):
        print("Drawing circle ({},{} with radius {})".format(x, y, radius))


class DrawApi2(object):
    def draw_circle(self, x, y, radius):
        print("Drawing circle 2 ({},{} with radius {})".format(x, y, radius))


class Circle(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self):
        self._radius *= percent


# Build
circle1 = Circle(1, 2, 3, DrawApi())

# Draw a circle
circle1.draw()

# Draw circle 2
circle2 = Circle(4, 6, 8, DrawApi())
# Draw a circle
circle2.draw()
