import os
#1
for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print("Cataloge:", os.path.join(dirpath, dirname))
    for filename in filenames:
        print('File:', os.path.join(dirpath, filename))
        
    print(os.stat(input('')))
    
#2
import os

path = input('')

if os.access(path, os.F_OK):
    print(f"The path '{path}' exists.")

if os.access(path, os.R_OK):
    print(f"The path '{path}' is readable.")

if os.access(path, os.W_OK):
    print(f"The path '{path}' is writable.")

if os.access(path, os.X_OK):
    print(f"The path '{path}' is executable.")

#3
import os
path = input('')

if os.access(path, os.F_OK):
    print(f"The path {path} exists.")
else:
    print(f"The path {path} does not exist.")
    
file_path = input('')

filename = os.path.basename(file_path)
print('Filename:', filename)

dir = os.path.dirname(file_path)
print('Directory:', dir)

#4
file_path = input("Enter path:")
lineCount = 0

with open(file_path, 'r') as file:
    for line in file:
        lineCount += 1
print("Number of lines in the file:", lineCount)

#5
import os

myLis = [1, 2, 3, 4]
fileName = input('')

outfile = open(fileName, 'w')
outfile.writelines([str(i)+'\n' for i in myLis])
outfile.close()

#6
import string

alphabet = string.ascii_uppercase
for letter in alphabet:
    with open(letter+'.txt', 'w') as file:
        file.remove(letter)
        
#7
with open('file1.txt', 'r') as fileone, open('file2.txt', 'a') as file2:
    for line in fileone:
        file2.write(line)

#8
import os

path = input('Enter path: ')

if os.path.exists(path):
    os.remove(path)
else:
    print("This path doesn't exist")
