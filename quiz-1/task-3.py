import random

def writeToFile(x):
    a = open("task-3.txt", 'w')
    a.write("Luwi elementebi: " + str(x[0]) + '\n' + "Kenti elementebi: " + str(x[1]) + '\n' + "3-is jeradebi: " + str(x[2]))
    a.close()

def fillTuple(t):
    for i in range(0, 100):
        t += (random.randint(0, 1000),)
    return t

def splitTuple(t):
    tuple_1 = ()
    tuple_2 = ()
    tuple_3 = ()
    for i in t:
        if i%2 == 0:
            tuple_1 += (i,)
        elif i%3 == 0:
            tuple_3 += (i,)
            tuple_2 += (i,)
        else:
            tuple_2 += (i,)
    return tuple_1, tuple_2, tuple_3
myTuple = fillTuple(())
writeToFile(splitTuple(myTuple))