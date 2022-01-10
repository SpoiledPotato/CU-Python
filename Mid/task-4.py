def filterTuple(t):
    resTuple = ()
    for el in t:
        if el.count('d') > 0 or el.count('o') > 0:
            resTuple += (el,)
    return resTuple


myTuple = ("iyo", "da", "ara", "iyo", "ra", "irakli", "orkestri", "didgori", "kata", "kurdgeli")
filteredTuple = filterTuple(myTuple)
print(filteredTuple)