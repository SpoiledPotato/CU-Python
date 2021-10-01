def oddTuples(aTuple):
    oddElements = ()
    for t in range(0, len(aTuple)):
        if t%2 == 0:
            oddElements += (aTuple[t],)
    return oddElements

print(oddTuples(('I','am','a','test','tuple')))