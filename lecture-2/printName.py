def printName(name, secName, reverse=True):
    if reverse: #reverse == true
        print(secName, name)
    else:
        print(name, secName)

printName("Irakli", "Tulashvili", False)