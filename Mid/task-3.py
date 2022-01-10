def cubeRoot(x):
    low = 1.0
    high = x
    epsilon = 0.01
    myGuess = x/2.0

    while abs(myGuess**3 - x) > epsilon:
        if myGuess**3 > x:
            high = myGuess
            myGuess = myGuess - (myGuess-low)/2.0
        elif myGuess**3 < x:
            low = myGuess
            myGuess = myGuess + (high-myGuess)/2.0
    return myGuess

print(cubeRoot(729))