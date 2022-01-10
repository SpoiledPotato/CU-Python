def gcd(a, b):
    c = 0
    if min(a, b) < max(a, b) // 2:
        c = min(a, b)
    else:
        c = max(a, b) // 2

    while a % c != 0 or b % c != 0:
        c -= 1
    return c


print(gcd(70, 140))
