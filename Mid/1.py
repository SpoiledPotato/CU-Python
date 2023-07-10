def findSubstring(s):
    biggestSubstring = s[0]
    biggestLength = 1
    currentSubstring = s[0]
    currentLength = 1

    for i in range(len(s)-1):
        print(i, s[i], biggestSubstring, currentSubstring)
        if len(s)-1 == i+1:
            print("FIRST")
            if s[i] < s[i+1]:
                print("->CHILD")
                currentSubstring += s[i+1]
                currentLength += 1

        if s[i] >= s[i+1] or (i+1) == (len(s)-1):
            print("SECOND")
            if currentLength > biggestLength:
                print("->CHILD")
                biggestLength = currentLength
                biggestSubstring = currentSubstring
            currentLength = 1
            currentSubstring = s[i+1]

        else:
            print("THIRD")
            if s[i] < s[i+1]:
                print("->CHILD")
                currentSubstring += s[i+1]
                currentLength += 1

    return biggestSubstring


a = findSubstring('yzabdecabcdefw')
print(a)
