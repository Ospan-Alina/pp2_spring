#1

import math

n = int(input())

print(((math.pi*n)/180))

#2
h, b1, b2 = int(input()), int(input()), int(input())

print(((b1+b2)*h)/2)

#3
import math

def calc(n ,l):
    A = (n * (l**2))/(4 * math.tan(math.pi / n))
    return A
    
n = int(input())
l = int(input())
    
A = calc(n, l)
    
print(int(A))

#4
a = int(input())
b = int(input())

Area = a * b

print(Area)
