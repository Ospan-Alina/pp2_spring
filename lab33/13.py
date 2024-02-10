import random

def guess():
    print('Hello! What is your name?')
    name = input()

    print('Well,', name, ', I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    n = random.randint(1, 20)

    cnt = 0
    
    while True:
        cnt += 1
        num = int(input())
        if num < n:
            print('Your guess is too low.')
            print('Take a guess.')
        elif num > n:
            print('Your guess is too high.')
            print('Take a guess.')
        else:
            print('Good job,', name, '! You guessed my number in', cnt, 'guesses!')
            break
        
guess()