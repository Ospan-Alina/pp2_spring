#1
class a:
    def init(self):
        self.string= ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

b = a()
b.getString()
b.printString()

#2
class shape:
    def init(self):
        pass
    
    def area(self):
        return 0

class square(shape):
    def init(self, length):
        super().init()
        self.length = length
    
    def area(self):
        return self.length  

Shape = shape()
print(Shape.area())

Square = square(5)
print(Square.area())

#3
class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(3, 4)
print(rectangle.area())

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self): # to display the coordinates of the point
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y): #to change these coordinates
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Test the class
point1 = Point(1, 2)
point2 = Point(3, 4)

point1.show()
point1.move(5, 6)
point1.show()

print(point1.dist(point2))

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}, {self.balance}")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount},{self.balance}")

account = Account("Alua", 1000)

account.deposit(100)
account.withdraw(200)
account.withdraw(300)
account.deposit(400)  

#6
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test list
num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

primeNumbers = list(filter(lambda x: prime(x), num_list))

print(primeNumbers)