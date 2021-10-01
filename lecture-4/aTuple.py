def aTuple(t):
    a = ()
    b = ()
    for i in range(0, len(t)):
        a += (t[i][0],) # numbers
        if t[i][1] not in b:
            b += (t[i][1],) # text
    return (a, min(a), max(a)), (b, len(b))
        

t = ((5,"hi"),(1,"hi"),(8,"no"),(12,"good"))
print(aTuple(t))