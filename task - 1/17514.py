from itertools import *

graph='ce ea ab bh hf fd dc cg eg gf ah'.split()
matrix='247 148 578 126 38 47 136 235'.split()

print(*range(1,9))
for i in permutations('abcdefgh'):
    if all(str(i.index(y)+1) in matrix[i.index(x)] for x,y in graph):
        print(*i)