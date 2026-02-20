from math import *
for n in range(1,10000000):
    i=ceil(log2(n))
    l=2783
    I=ceil(i*l/8)
    if I*3_845_627 >= 11*2**30:
        print(n)
        break