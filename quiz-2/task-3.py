def myCount(str, substr):
    l = len(substr)
    count = 0
    for i in range(0, len(str)-l+1):
        if str[i:i+l] == substr:
            count += 1
    return count

s = "hihellohellonohellon"
w = "hello"

print(myCount(s, w))
