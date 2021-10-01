# def pal(a):
#     return a==a[::-1]
# print(pal("madam"))

def pal(x):
    if len(x) < 2: return True
    if x[0] != x[-1]: return False
    return pal(x[1:-1])

print (pal('madam'))