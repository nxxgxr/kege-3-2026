from itertools import *
graph='db bf fc cg ga ad ge ce fe be'.split()
matrix='47 357 2567 16 236 345 123'.split()
print(*range(1,8))
for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)