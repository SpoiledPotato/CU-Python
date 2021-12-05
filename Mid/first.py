# inp = input("Enter your age:")
# inp = int(inp)

# if inp >= 1 and inp <= 5:
#     print("shen dadixar bagshi")
# elif inp >=6 and inp <=17:
#     print("skola")
# elif inp >=18 and inp <=22:
#     print("uni")
# else: 
#     print ("daberdi")


# inp = input("Enter num:")
# dg = input("Enter degree:")
# inp = int(inp)
# dg = int(dg)


# i = 1
# while(i < dg):
#     res = res * inp
#     i = i + 1
# print(res)

# res = inp
# for i in range(1, dg):
#     res = res * inp
# print(res)
      # 0, 1, 2, 3,    4

lst = [1, 2, 4, 3, "gvantsa"]
tpl = (1, 2, 3, 4, "hello")



# st = "gvantsa saintereso adamiania, dzalian."

s = "acfdert"

biggestSubString = 1
res = 1
for i in range(0, len(s)-1):
      if s[i] < s[i+1]:
            res += 1
      if i == len(s)-2 or s[i] >= s[i+1]:
            if(biggestSubString < res):
                  biggestSubString = res
                  res = 1
            
print(biggestSubString)
# for el in s:
#       print(el)
