from math import *
for i in range(1,1000):
    L=377
    I=ceil(i*L/8)
    if I*23155>5536*2**10:
        print(2**(i-1) +1)
        break
