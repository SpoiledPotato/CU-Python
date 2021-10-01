a=open("hi.txt", "w")
for i in range(0,5):
    a.write(input("Enter text for line " + str(i+1) + ": ") + "\n")

a.close()

a=open("hi.txt", "r")
b=a.read()
print(b)
a.close()