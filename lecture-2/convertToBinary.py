# decimalNum = 19
# binaryNum = ''
# while decimalNum > 0:
#     print(decimalNum)
#     if decimalNum % 2 == 1:
#         binaryNum += '1'
#     else:
#         binaryNum += '0'
#     decimalNum //= 2
# print(binaryNum[::-1])

num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
    # if isNeg:
    #     #something