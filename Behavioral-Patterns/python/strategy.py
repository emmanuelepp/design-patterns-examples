# Strategy
# Lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
import types


class Stratey:
    def __init__(self, function=None):
        self.name = "Default Strategy"

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print('{} is used'.format(self.name))

# Replacement method 1


def strategy_one(self):
    print('{} is used to exec method one'.format(self.name))

# Replacement method 2


def strategy_two(self):
    print('{} is used to exec method two'.format(self.name))


# Create default strtegy
s0 = Stratey()

# Execute

s0.execute()

# Create variation

s1 = Stratey(strategy_one)

s1.name = 'Strategy one'

# Execute strategy

s1.execute()

s2 = Stratey(strategy_two)
s2.name = 'Strategy two'

s2.execute()
