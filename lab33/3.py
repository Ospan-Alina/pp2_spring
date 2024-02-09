numheads, numlegs = 36, 94

def solve(numheads, numlegs):
    for c in range(numheads):
        r = 35 - c
        numlegs = c * 2 + 4 * r
        if numlegs == 94:
            print(c, r)
        
solve(numheads, numlegs)

#c - chicken
 #r - rabbit   
    