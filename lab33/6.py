def reverse(txt):
    word = txt.split()
    words = word[::-1]
    sent = ' '.join(words)
    return sent

txt = input()
print(reverse(txt))


