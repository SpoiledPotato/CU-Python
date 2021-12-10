class Fraction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "/" + str(self.y)

    def __add__(self, other):
        return Fraction(((self.x*other.y) + (other.x*self.y)), (self.y*other.y))


first = Fraction(1, 2)
second = Fraction(2, 3)
print(first)
foo = first + second
print(foo)