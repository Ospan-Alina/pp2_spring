#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2
fruits = ["apple", "banana", "cherry"]
fruits = "kiwi"
#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

"""
    Examples:
    To determine how many items a list has, use the len() function
    """
#1
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#2 also its possible to use the list() constructor to create a new list
thislist = list(("apple", "banana", "cherry"))
print(thislist)
#3 also we can print list elements one by one using a loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#4  append() adds an element to the end of the list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#5 sort() method that will sort the list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#6 Make a copy of a list  we can use method copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

