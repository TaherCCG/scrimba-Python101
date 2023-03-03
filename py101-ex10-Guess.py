print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guess number and number of guesses
#3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins


# my version
num=78
guess=0
noOfGuess=int(input("How many guesses you like? :"))
gNum=0

while gNum < noOfGuess:
    guess = int(input(f'Guess #{gNum+1}. Guess a number 1-100:'))
    if guess == num:
        print("You win!!")
        break    
    elif guess < num:
        print (f"too low try again, your guess:{guess} ")
        gNum+=1
    elif guess > num:
        print(f"too high, try again, your guess:{guess} ")
        gNum+=1
    
if gNum == noOfGuess:
    print(f"You had {noOfGuess} guesses, and didn't any right. number was {num}")


# version 2 (solution)
num = 76
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-100: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')
