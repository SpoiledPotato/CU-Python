a=[5,6,12,1,18]
print(a[0], a[-1])
for i in range(0,len(a)):
    print(a[i])
print("-----------")
for i in a:
    print(i)
print("---------")
a[2]=200
print(a)
a.append(500)
print(a)
#a.sort()
print(sorted(a))
print(a)
a.reverse()
print(a)
print(sum(a),max(a),min(a))
print(a.count(5))
a.revers(5)
print(a)
a.insert(2,100)
print(a)
a.pop(1)
print(a)
b = "hello, my name is"
print(a.split())
print(a.split(" "))