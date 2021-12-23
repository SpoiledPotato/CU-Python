import random


def dictDetails(dict):
    tList = []
    mostEls = {'key': '', 'size': 0}
    mult = 1
    for key in dict:
        tList.extend(dict[key])
        size = len(dict[key])
        if size > mostEls['size']:
            mostEls['key'] = key
            mostEls['size'] = size
    for n in tList:
        mult *= n
    return mostEls['key'], mult


def dictFill(dict):
    t = [1, 1, 4, 7]
    k = ord('a')
    for i in range(sum(t)):
        r = random.randint(1, 100)
        myDict[chr(k)].append(r)
        t[0] -= 1
        if t[0] <= 0:
            t.pop(0)
            k += 1
    return dictDetails(dict)


myDict = {'a': [], 'b': [], 'c': [], 'd': []}

print(dictFill(myDict))
