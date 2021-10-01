a={"gio":90, "dato":80, "lana":91, "roma":96}

print(a["gio"])
print("dato" in a)
for i, j in a.items():
    print(i)
    print(j)

a[7] = 100
print(a)
a[8] = "hi"
print(a)

for i in a:
    print(i)

print(a.keys())
print(a.values())