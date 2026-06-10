from itertools import *

def f(x,y):
    return ((x<a) and (y<3*a)) or (2*x +y >128)

for a in range(1,100):
    if all(f(x,y) for x in range(1,5000) for y in range(1,5000)):
        print(a)
        break