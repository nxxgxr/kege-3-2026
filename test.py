hw=2560*1440
i=22

hw2=1920*1080
i2= 20

i1=hw*i
i2=hw2 * i2
v=(i1 - i2)/2**13 * 130
from math import *

# print(v)




from math import *
for l in range(1,10**5):
    i=ceil(log2(10+27))
    I=ceil(i*l/8)
    if I*3548>12*2**10:
        print(l)
        break
