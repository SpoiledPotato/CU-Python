def draw(rowCount):
    row = ''
    x = ord('a')

    while rowCount > 0:
        row += chr(x)
        if x == ord('z'):
            x = ord('a')
        else:
            x += 1
        print(row)
        rowCount -= 1


rows = int(input("Enter row count: "))

draw(rows)