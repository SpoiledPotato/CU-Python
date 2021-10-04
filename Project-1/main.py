import vigenere_list
import vigenere_string
import vigenere_tuple
# 65

myString = "attackatdawn"
myTuple = ("irakli", "tulashvili", myString)
myKey = "LEMON"

encryptedString = vigenere_string.encrypt(myString, myKey)
decriptedString = vigenere_string.decrypt(encryptedString, myKey)

encryptedTuple = vigenere_tuple.encrypt(myTuple, myKey)
decryptedTuple = vigenere_tuple.decrypt(encryptedTuple, myKey)

# print(myString)

# print(encryptedString)
# print(decriptedString)

print(myTuple)
print(encryptedTuple)
print(decryptedTuple)

# print(ord("A"))
