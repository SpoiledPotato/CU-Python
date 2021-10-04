import vigenere_list, vigenere_string, vigenere_tuple
# 65

myString = "attackatdawn"
myKey = "LEMON"

encryptedString = vigenere_string.encrypt(myString, myKey)
print(encryptedString)
decriptedString = vigenere_string.decrypt(encryptedString, myKey)
print(decriptedString)

s = "A"
k = "L"

# print(ord("A"))