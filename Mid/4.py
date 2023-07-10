def filterTuple(t):
    resTuple = ()
    for el in t:
        if el.count('d') > 0 or el.count('o') > 0:
            resTuple += (el,)
    return resTuple


myTuple = ("lorem", "ipsum", "dolor", "sit", "amet", "meti", "agar", "vici", "avto", "gurgenidze")
filteredTuple = filterTuple(myTuple)
print(filteredTuple)