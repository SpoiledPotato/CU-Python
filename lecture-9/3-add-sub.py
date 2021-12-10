class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.y-other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    def __str__(self) -> str:
        return "<" + str(self.x) + "," + str(self.y) + ">"
        
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

c = Coordinate(3, 4)
origin = Coordinate(1, 2)

foo = c-origin
foo2 = c+origin
print(foo)
print(foo2)