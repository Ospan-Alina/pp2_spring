def spy_game(mystring):
    if '007' in mystring:
        print('True')
    else:
        print('False')
        
numbers = [1,7,2,0,4,5,0]
mystring = ""
for digit in numbers:
    mystring += str(digit)
    
subsrt = '007'
       
spy_game(mystring)


