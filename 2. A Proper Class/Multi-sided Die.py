import random

class MSDie:
    def __init__(self, sides):
        self.num_of_sides = sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_of_sides + 1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_of_sides, self.current_value)

    def __eq__(self, other):
        return self.current_value == other.current_value

    def __lt__(self, other):
        return self.current_value < other.current_value

    def __gt__(self, other):
        return self.current_value > other.current_value

    def __ne__(self, other):
        return self.current_value != other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value

    def __ge__(self, other):
        return self.current_value >= other.current_value

x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x > y)
print(x != y)
print(x<=y)
print(x>=y)
print(x is y)