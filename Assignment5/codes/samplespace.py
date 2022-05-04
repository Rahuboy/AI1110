#code to find sample space 1

from itertools import permutations

possibilities = ['A','B','C']

samplespace = permutations(possibilities,2)

print(*samplespace, sep=", ")
