import random

myList = []
for i in range(50):
    myList.append(random.randint(0,100))

def findOddNumbers(list):
    oddNums = []
    for i in list:
        if i%2 == 1:
            oddNums.append(i)
    return oddNums

def findOddPositions(list):
    oddPoss = []
    for i in range(0, len(list)):
        if(i%2 == 0):
            oddPoss.append(list[i])

