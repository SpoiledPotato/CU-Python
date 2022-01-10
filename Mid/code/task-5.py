def coreFib(n, d):
    if n in d:
        return d[n]
    else:
        ans = coreFib(n-1, d) + coreFib(n-2, d)
        d[n] = ans
        return ans

def countMonths(x):
    i = 2
    while coreFib(i, d) < x:
        i += 1
    return i

d = {1:1, 2:1}

n = 21
months = countMonths(n)

a = open("result.txt", "w")
a.write(str(n) + " kurdgeli iqneba " + str(months) + " tveshi.")
a.close()