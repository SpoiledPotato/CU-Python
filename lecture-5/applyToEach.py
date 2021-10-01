# def applyToEach(L, f):
#     for i in range(0, len(L)):
#         L[i]=f(L[i])
#     return L

# print(applyToEach([5, 6, -2, -8], abs))

def applytoeach(L,x):
    a=[]
    for f in L:
        a.append(f(x))
        print(a)

applytoeach([abs,int],-5.2)
