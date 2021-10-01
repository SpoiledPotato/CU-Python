# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)

# print(mult(5,4))

# a = 5
# b = 4
# while b > 1:
#     a = a + 5
#     b -= 1
# print(a)

# def fact(r):
#     res = 1
#     for i in range(1,r+1):
#         res *=i
#     return res

# print(fact(5))

# def fact(x, y=1):
#     if x == 1:
#         return y
#     else:
#         return fact(x-1, y*x)

# print(fact(5))

def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
print(fact(5))