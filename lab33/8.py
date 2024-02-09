def spy_game(mystring):
    if '007' in mystring:
        print('True')
    else:
        print('False')
        
numbers = [1,2,4,0,0,7,5]
mystring = ""
for digit in numbers:
    mystring += str(digit)
    
subsrt = '007'
       
spy_game(mystring)


