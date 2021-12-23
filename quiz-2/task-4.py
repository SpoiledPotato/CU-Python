def decToBin(dec):
    binary = ""
    while dec > 0:
        if dec % 2 == 1:
            binary += '1'
        else:
            binary += '0'
        dec //= 2
    return binary[::-1]


decimalNum = 27
print(decToBin(decimalNum))
