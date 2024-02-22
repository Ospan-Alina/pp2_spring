#1
'''
def square(n):
    for i in range(1, n + 1):
        yield i*i
        
n = int(input())

num = square(n)

for i in num:
    print(i)
    
    
#2
def even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
            
n = int(input())

num = even(n)
for i in num:
    print(i)
    
#3
def div(n):
    for i in range(0, n + 1):
        if i % 4 == i % 3 == 0:
            yield i
            
n = int(input())
num = div(n)
for  i in num:
    print(i)

#4
def square(n):
    for i in range(n, m + 1):
        yield i*i
        
n, m = int(input()), int(input())

num = square(n)

for i in num:
    print(i)
'''
#5
def down(n):
    for i in range(n, -1,-1):
        yield i
        
n = int(input())

num = down(n)

for i in num:
    print(i)

