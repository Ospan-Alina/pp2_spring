#1
from functools import reduce
import operator

def multiply_list(numbers):
    result = reduce(operator.mul, numbers, 1)
    return result

num_list = [int(x) for x in input().split()]
product = multiply_list(num_list)
print("Product of all numbers:", product)

#2
def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print("Upper case:", u,  "Lowercase:", l)
    
s = input()
up_low(s)
    
#3
def palindrome(s):
    rs = s[::-1]
    if s == rs:
        print("Polindrome")
    else:
        print("Not polindrome")
        
s = input()
palindrome(s)

#4
import math
a, b = int(input()), int(input())

print('Square root of', a, 'after', b, 'milliseconds is', math.sqrt(a))

#5
boolean_list1= [True, False]
boolean_list2 = [True, True]
print(all(boolean_list1))
print(all(boolean_list2))