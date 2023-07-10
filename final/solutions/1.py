class NewTuple(object):
    def __init__(self):
        self.tuple = ()

    def add(self, el):
        if el in self.tuple:
            self.tuple += (el,)

    def remove(self, el):
        self.tuple = self.tuple[:el] + self.tuple[el+1:]

    def __str__(self):
        return str(self.tuple)


myTuple = NewTuple()
myTuple.add('Johnny')
myTuple.add('Sins')
myTuple.add('Zukerburger')
print(myTuple)
myTuple.remove(1)
print(myTuple)
