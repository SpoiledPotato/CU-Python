def findSubstring(s):
    biggestSubstring = s[0]
    biggestLength = 1
    currentSubstring = s[0]
    currentLength = 1
    
    for i in range(0, len(s)-1):
        
        # if it's last element
        if len(s)-1 == i+1:
            if s[i] < s[i+1]:
                currentSubstring += s[i+1]
                currentLength += 1

        if s[i] >= s[i+1] or (i+1) == (len(s)-1):
            if currentLength > biggestLength:
                biggestLength = currentLength
                biggestSubstring = currentSubstring
                currentLength = 1
                currentSubstring = s[i+1]
        else:
            if s[i] < s[i+1]:
                currentSubstring += s[i+1]
                currentLength += 1
    
    return biggestSubstring
        
            

a = findSubstring('yzabdecw')
print(a)