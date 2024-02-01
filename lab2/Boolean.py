#1
print(10 > 9) 
True
#2
print(10 == 9)
False
#3
print(10 < 9)
False
#4
print(bool("abc"))
True
#5
# such as (), [], {}, "", the number 0, and the value None evaluates to False
print(bool(0))
False 
"""
Examples:
if you have an object that is made from a class
with a __len__ function that returns 0 or False
"""
#1
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#2 isinstance() function, which determine if an object is of a certain data type
x = 200
print(isinstance(x, int))