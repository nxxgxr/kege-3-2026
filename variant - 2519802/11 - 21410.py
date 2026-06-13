from math import *
for n in range(1,1000):
    i=ceil(log2(n))
    l=257
    I=ceil(i*l/8)
    if I*295_740 <=33 * 2**20:
        print(n)