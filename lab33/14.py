#1
n = int(input())

def ounces(n):
    print(n * 28.3495231)
    
ounces(n)

#2
f = int(input())

def cen(f):
    c = (5 / 9)*(f - 32)
    print(c)
    
cen(f)

#3
numheads, numlegs = 36, 94

def solve(numheads, numlegs):
    for c in range(numheads):
        r = 35 - c
        numlegs = c * 2 + 4 * r
        if numlegs == 94:
            print(c, r)
        
solve(numheads, numlegs)