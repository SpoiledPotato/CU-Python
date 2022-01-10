rows = int(input("Enter row count: "))

# print(c)
row = ''
x = ord('a')

for i in range(0, rows):
    row += chr(x)
    if x == ord('z'):
        x = ord('a')
    else:
        x += 1
    print(row)