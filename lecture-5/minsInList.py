L1 = [1, 28, 36]
L2 = [2, 57, 9]

L3 = []
for elt in map(min, L1, L2):
    L3.append(elt)

print(L3)