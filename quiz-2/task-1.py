class lists(object):
    def __init__(self, list):
        self.list = list

    def min(self):
        minimum = self.list[0]
        for el in self.list:
            if el < minimum:
                minimum = el
        return minimum

    def max(self):
        maximum = self.list[0]
        for el in self.list:
            if el > maximum:
                maximum = el
        return maximum

    def sum(self):
        summed = 0
        for el in self.list:
            summed += el
        return summed

    def __str__(self):
        return str(self.sum()) + ' ' + str(self.min()) + ' ' + str(self.max())


myList = [1, 2, 3, 4]
c = lists(myList)
print(c)
