from itertools import *

matrix = '24 134 267 125 47 37 356'.split()
graph = 'ag ge eb bd dc cf fa fg cb'.split()
print(*range(1, 8))
for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
