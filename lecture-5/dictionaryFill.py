import random
a = {}
for i in range(0, 10):
    a[random.randint(1, 100)] = random.randint(100, 200)

print(a)