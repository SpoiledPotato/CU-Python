list = (2, 8, 64, 16, 32, 4, 16, 8)
print(len(list))
print(len(set(list)))
if len(list) > len(set(list)):
    print("The list provided contains duplicate values")