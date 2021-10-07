import Components.vigenere


def encrypt(T, key):
    encryptedTuple = ()
    for s in T:
        encryptedString = Components.vigenere.encrypt(s, key)
        encryptedTuple += (encryptedString,)
    return encryptedTuple


def decrypt(T, key):
    decryptedTuple = ()
    for s in T:
        decryptedString = Components.vigenere.decrypt(s, key)
        decryptedTuple += (decryptedString,)
    return decryptedTuple


inp = input("Do you want to (E)NCRYPT or (D)ECRYPT the text?: ")
tmpTuple = ()
if inp == 'E' or inp == 'e':
    n = int(input("How many elements do you want to have in tuple?: "))
    for i in range(0, n):
        tmpTuple += (input("Enter element #" + str(i) + ": "),)
    encryptedList = encrypt(tmpTuple, input("Enter key: "))
    print("Encrypted list:", encryptedList)
elif inp == 'D' or inp == 'd':
    n = int(input("How many elements do you want to have in tuple?: "))
    for i in range(0, n):
        tmpTuple += (input("Enter element #" + str(i) + ": "),)
    decryptedList = decrypt(tmpTuple, input("Enter key: "))
    print("Decrypted list:", decryptedList)
