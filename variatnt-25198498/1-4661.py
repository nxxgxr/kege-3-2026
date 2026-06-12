from itertools import *

graph = 'be eg gh ha ab bc ad dc fg fe'.split()
matrix = '68 568 457 35 234 12 38 127'.split()
print(*range(1, 9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
