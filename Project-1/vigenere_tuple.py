import vigenere_string


def encrypt(T, key):
    encryptedTuple = ()
    for s in T:
        encryptedString = vigenere_string.encrypt(s, key)
        encryptedTuple += (encryptedString,)
    return encryptedTuple


def decrypt(T, key):
    decryptedTuple = ()
    for s in T:
        decryptedString = vigenere_string.decrypt(s, key)
        decryptedTuple += (decryptedString,)
    return decryptedTuple
