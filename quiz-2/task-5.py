def binToDec(binary):
    l = len(binary)
    d = 0
    try:
        for i in range(l):
            d += int(binary[-i-1]) * (2 ** i)
    except:
        raise ValueError('incorrect binary number')
    return d


myBinary = "1101"
print(binToDec(myBinary))
