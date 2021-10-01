def applyToEach(L, f):
    for i in range(len(L)):
        print(f(L[i]))

def mult(x):
    return x*5
testList = [1, -4, 8, -9]
applyToEach(testList, mult)