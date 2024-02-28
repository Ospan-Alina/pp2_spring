import re
#1
n = input()

n = re.search("ab*", n)
if n:
    print("match")
else:
    print("doesn't match")

    
#2
n = input()

n = re.search("aabbb+", n)
if n:
    print("match")
else:
    print("doesn't match")
    
    
#3
import re

n = input()
n = re.search(r"[a-z]+[_][a-z]+", n)

if n:
    print("match")
else:
    print("doesn't match")


#4
import re

n = input()
n = re.search(r"[A-Z]+[a-z]+", n)

if n:
    print("match")
else:
    print("doesn't match")

#5
import re

n = input()
n = re.search("a..b", n)

if n:
    print("match")
else:
    print("doesn't match")
    
    
#6
import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result

input_text = input("Enter a string: ")
output_text = replace_with_colon(input_text)
print("Result:", output_text)


#7
test_str = input()

temp = test_str.split('_')

res = temp[0] + ''.join(ele.title() for ele in temp[1:])
     
print(str(res))

#8
import re

def split_at_uppercase(text):
    pattern = r'[A-Z]'
    indices = [match.start() for match in re.finditer(pattern, text)]
    parts = [text[i:j] for i, j in zip([0] + indices, indices + [None])]
    parts = [part for part in parts if part]
    return parts

input_text = input("Enter a string: ")
result = split_at_uppercase(input_text)
print("Result:", result)

#9
import re

def insert_spaces(text):
    pattern = r'(?<!\b)(?=[A-Z])'
    result = re.sub(pattern, ' ', text)
    return result

input_text = input()
result = insert_spaces(input_text)
print("Result:", result)

#10

import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

camel_case_string = input("Enter a camel case string: ")
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case:", snake_case_string)
