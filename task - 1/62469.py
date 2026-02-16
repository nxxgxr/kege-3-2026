from itertools import *
graph='fh hc ce eb bd df bg eg ga ca af'.split()
matrix='38 678 156 78 367 235 245 124'.split()
print(*range(1,9))
for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)