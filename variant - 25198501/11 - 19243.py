from math import *

for i in range(1,1000):
    l=377
    I=ceil(i*l/8)
    if 23_155*I>5536*2**10:
        print(2**(i-1) + 1)
        break
