import Components.vigenere


def encrypt(L, key):
    encryptedList = []
    for s in L:
        encryptedString = Components.vigenere.encrypt(s, key)
        encryptedList.append(encryptedString)
    return encryptedList


def decrypt(L, key):
    decryptedList = []
    for s in L:
        decryptedString = Components.vigenere.decrypt(s, key)
        decryptedList.append(decryptedString)
    return decryptedList


inp = input("Do you want to (E)NCRYPT or (D)ECRYPT the text?: ")
tmpList = []
if inp == 'E' or inp == 'e':
    n = int(input("How many elements do you want to have in list?: "))
    for i in range(0, n):
        tmpList.append(input("Enter element #" + str(i) + ": "))
    encryptedList = encrypt(tmpList, input("Enter key: "))
    print("Encrypted list:", encryptedList)
elif inp == 'D' or inp == 'd':
    n = int(input("How many elements do you want to have in list?: "))
    for i in range(0, n):
        tmpList.append(input("Enter element #" + str(i) + ": "))
    decryptedList = decrypt(tmpList, input("Enter key: "))
    print("Decrypted list:", decryptedList)
