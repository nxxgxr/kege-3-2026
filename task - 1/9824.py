from itertools import *

graph='eg gd df fa ab bc ce ed ca'.split()
matrix='346 45 16 125 247 137 56'.split()
print(*range(1,9))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
