def palindrome(txt):
    txt1 = txt[::-1]
    if txt1 == txt:
        print('palindrome')
    else:
        print('not palindrome')

txt = input()
palindrome(txt)


