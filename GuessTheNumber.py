#this is a guess the number game
import random
secretNumber = random.randint(1,20)
print('Im thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber: 
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is to high')
    else:
        break #this condition is the correct guess!

if guess == secretNumber:
    print('Great job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
