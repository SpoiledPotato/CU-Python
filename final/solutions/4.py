def gcd(a, b):
    if b == 0:
        return a
    else:
        return (gcd(b, a % b))


print(gcd(6, 12))
print(gcd(120, 2500))
