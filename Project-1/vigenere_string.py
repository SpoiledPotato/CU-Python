import Components.vigenere


def encrypt(S, key):
    return Components.vigenere.encrypt(S, key)


def decrypt(S, key):
    return Components.vigenere.decrypt(S, key)


inp = input("Do you want to (E)NCRYPT or (D)ECRYPT the text? ")
if inp == 'E' or inp == 'e':
    encryptedText = encrypt(input("Enter text: "), input("Enter key: "))
    print("Encrypted text:", encryptedText)
elif inp == 'D' or inp == 'd':
    decryptedText = decrypt(input("Enter text: "), input("Enter key: "))
    print("Decrypted text:", decryptedText)
