from math import *
for n in range(1,10*8):
    i=ceil(log2(n))
    l=211
    I=ceil(i*l/8)
    if I*23654 <= 3241*2**10:
        print(n)