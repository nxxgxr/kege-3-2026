from math import *
for l in range(1,10000000):
    n=10+52+500
    i=ceil(log2(n))
    I=ceil(i*l/8)
    if I*45877>=49*2**20:
        print(l)
        break