from itertools import *
print(*range(1,9))
graph='ah hf fe eg gb ba bc gc cd df'.split()
matrix='47 458 67 125 246 35 138 27'.split()
for i in permutations('abcdefgh'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)