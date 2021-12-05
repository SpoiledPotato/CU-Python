def filterTuple(t):
    modifiedTuple = ()
    for i in t:
        if i.find('a') >= 0 or i.find('b') >= 0:
            modifiedTuple += (i,)
    return modifiedTuple


myTuple = ("irakli", "kargi", "chkviani", "simpatiuri", "da", "sxva", "bichia", "pitoni",
           "kargi", "programirebis", "enaa", "romelic", "somxeti", "ruseti", "ukraina")
print(filterTuple(myTuple))
