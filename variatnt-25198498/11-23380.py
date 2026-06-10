from math import *
for l in range(1,10000):
    i=ceil(log2(10+17))
    I=ceil(i*l/8)
    if I*7_564_230>31*2**20:
        print(l)
        break
