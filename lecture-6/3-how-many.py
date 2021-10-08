def how_many(aDict):
    x = 0
    for i in aDict.values():
        x += len(i)
    return x


def biggest(aDict):
    biggest = 0
    collection = []
    if len(aDict) == 0:
        return None
    for e in aDict:
        if len(aDict[e]) >= biggest:
            biggest = len(aDict[e])
            collection = e
    return collection


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
print(biggest(animals))
