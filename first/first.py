'''print ("hello", "no")
print ("5+2=",5+2)
print ("5-2=",5-2)
print ("5*2=",5*2)
print ("5/2=",5/2)
print ("5//2=",5//2)
print ("5**2=",5**2)
print ("nashti:",5%2)'''

'''a=5
b=2
c="hello"
d=2.8
print ("a=",a)
print ("b=",b)
print ("a+b=",a+b)
print (type(a))
print (type(c))
print (type(d))'''

# a = input("sheikvane user: ")
# b = input("sheikvane paroli: ")
# if a == 'user' and b == 'passw':
#     print("wellcum")
# elif a == 'user' or b == 'passw':
#     print("try again")
# else:
#     print("haker detected")

# s = "azcbobobegghaki"
# i = 0
# n=0
# while i < len(s):
#     if s[i:i+3] == "bob":
#         n = n + 1
#     i = i + 1
# print(n)

# numBobs = 0
# for i in range(1, len(s)-1):
#     if s[i-1:i+2] == "bob":
#         numBobs += 1
# print("Number of times bob occurs in '" + s + "' is:", numBobs)


# s = "azcbobobegghakl"
# str = ''
# tmp = ''
# o1 = 1
# o2 = 1
# i = 1
# while i < len(s)-1:
#     print("Main loop, i =", i)
#     while s[i] >= s[i-1] and i < len(s)-1:
#         print("inside loop, i =",i)
#         print("s[i]=",s[i], "s[i-1]=",s[i-1])
#         tmp += s[i]
#         i += 1
#     print("\n")
#     if len(tmp) > len(str):
#         str = tmp
#     tmp = ''
#     i += 1
# print(str)

# i = 0
# num = 3
# out = 0
# while i < num:
#     out += num
#     i += 1
# print(str(num) + "*" + str(num) + " = " + str(out))


# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if x < 0:
#         ans = - ans
# print(ans)

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses, 'guess =', guess)