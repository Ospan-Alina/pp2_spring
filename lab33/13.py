import random


print('Hello! What is your name?')
name = input()

print('Well,', name, ', I am thinking of a number between 1 and 20.')
print('Take a guess.')
n = random.randint(1, 20)

num = int(input())
def guess(n):
    cnt = 0
    if num < n:
        cnt += 1
        print('Your guess is too low.')
        print('Take a guess.')
        return guess(n)
    elif num > n:
        cnt += 1
        print('Your guess is too high.')
        print('Take a guess.')
        return guess(n)
    else:
        print('Good job,', name, '! You guessed my number in', cnt, 'guesses!')
        
guess(n)