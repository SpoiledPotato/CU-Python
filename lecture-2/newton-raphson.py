epsilon = 0.01
y = 2400.0
guess = y/2.0
numGesses = 0
while abs(guess*guess - y) >= epsilon:
    numGesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))
print('numGuesses = ' + str(numGesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))