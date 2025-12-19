from itertools import *

graph='ав аб бв вд де ек кг гв ав ег'.split()
matrix='24 146 56 1267 36 23457 46'.split()

for i in permutations('абвгдек'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
