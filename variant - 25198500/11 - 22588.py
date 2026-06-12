from math import *
for v in range(1,1000):
    i=ceil(log2(10+52+70))
    l=18
    I=ceil(i*l/8) + v
    if I*2000<=100*2**10:
        print(v)

