from itertools import *
graph='gd dc db cb ca ba ce bf ef'.split()
matrix='4 56 67 156 2467 2345 35'.split()
print(*range(1,8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
