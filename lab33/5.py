import itertools

def print_permutations(str):
    string_permutations = itertools.permutations(str)
    string_permutations = [''.join(permutation) for permutation in string_permutations]
    print(string_permutations)
    
str = input()

print_permutations(str)

