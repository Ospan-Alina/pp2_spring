def unique(lst):
    numbers = []
    for i in lst:
        if i not in numbers:
            numbers.append(i)
    return numbers
        
lst = [1, 2, 2, 3]

print(unique(lst))