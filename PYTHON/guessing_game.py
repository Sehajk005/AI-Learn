import random
jackpot = random.randint(1, 100)
guess = int(input('Pick a number between 1 to 100: '))

count = 1
while guess != jackpot:
    if guess>jackpot:
        print('Guess lower')
    else:
        print('Guess higher')
    guess = int(input('try again: '))
    count+=1
print('bravo!', count)