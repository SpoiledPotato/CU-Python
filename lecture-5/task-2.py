a=["gio", "gio", "saba", "gio", "saba", "nino"]
b={}
for i in a:
    if b.get(i):
        b[i] += 1
    else:
        b[i] = 1

print(b)

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

print(lyrics_to_frequencies(a))