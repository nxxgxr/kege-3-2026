from itertools import *

graph='gb be ef fd dc ca ag cf ab'.split()
matrix='246 16 57 15 347 127 356'.split()

print(*range(1,9))

for i in permutations('abcdefg'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
