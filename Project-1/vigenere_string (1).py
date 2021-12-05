def getFullKey(key, length):
    fullKey = key
    for i in range(len(key), length):
        fullKey += key[i % len(key)]
    return fullKey


def encrypt(S, key):
    S = S.upper()
    key = key.upper()
    fullKey = getFullKey(key, len(S))
    encryptedString = ""
    for i in range(0, len(S)):
        a = ord(S[i])-65
        b = ord(fullKey[i])-65
        encryptedString += chr((a+b) % 26 + 65)

    return encryptedString


def decrypt(S, key):
    S = S.upper()
    key = key.upper()
    fullKey = getFullKey(key, len(S))
    decryptedString = ""
    for i in range(0, len(S)):
        a = ord(S[i])-65
        b = ord(fullKey[i])-65
        decryptedString += chr((a-b) % 26 + 65)

    return decryptedString
