import random

def withFor(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def withWhile(x):
    result = 1
    i = 1
    while i <= x:
        result *= i
        i += 1
    return result

def withRecursion(x):
    if x == 1:
        return 1
    else:
        return x * withRecursion(x-1)

number = 5
r = random.randint(0,2)
print('r =', r)
if r == 0:
    print("Counting factorial of", number, "using for loop...")
    print(withFor(number))
elif r == 1:
    print("Counting factorial of", number, "using while loop...")
    print(withWhile(number))
else:
    print("Counting factorial of", number, "using recursion...")
    print(withRecursion(number))