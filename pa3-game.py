
import random
secret_number = random.randint(1,100)
tries = 0

print('Welcome to the random number guessing game!')
lives = int(input('How many lives would you like peko: '))
while lives > 0:
    guess = int(input('Please guess a number between 1-100 peko: '))
    if guess != secret_number:
        lives -= 1
        tries += 1
        if guess < secret_number:
            print('Too smol')
        if guess > secret_number:
            print('Too BEEEEEG')
        print('You have ' + str(lives) + ' ' + 'live(s) left.')
        continue
    if guess == secret_number:
        print('You win, and all it took you was ' + str(tries) + ' tries peko.')

print('You lost HAHAHAHA')
print('The answer was: ' + str(secret_number))

'''
print('Welcome to the random number guessing game!')
lives = int(input('How many lives would you like peko: '))
while True:
    guess = int(input('Please guess a number between 1-100 peko: '))
    if guess =
    = secret_number:
        print('You win, and all it took you was ' + str(tries) + ' tries peko.')
        break
    lives -= 1
    tries += 1
    if guess < secret_number:
        print('Too smol')
    if guess > secret_number:
        print('Too BEEEEEG')
    print('You have ' + str(lives) + ' ' + 'live(s) left.')
    if lives == 0:
        print('You lost HAHAHAHA')
        print('The correct answer was: ' + str(secret_number))
        break
'''






