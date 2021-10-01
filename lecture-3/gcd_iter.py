# def gcd(a, b):
#     tmp = min(a,b)
#     while b%tmp != 0 or a%tmp != 0:
#         tmp -= 1
#     return tmp

# print(gcd(15,25))

def gcdIter(a, b):
    c = min(a,b)
    while c > 0:
        if(a%c) == 0 and (b%c) == 0:
            return c
        else:
            c -= 1

print(gcdIter(15,25))