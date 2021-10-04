import vigenere_string

def encrypt(L, key):
    encryptedList = []
    for s in L:
        encryptedString = vigenere_string.encrypt(s, key)
        encryptedList.append(encryptedString)
    return encryptedList

def decrypt(L, key):
    decryptedList = []
    for s in L:
        decryptedString = vigenere_string.decrypt(s, key)
        decryptedList.append(decryptedString)
    return decryptedList