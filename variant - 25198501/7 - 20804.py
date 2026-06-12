from math import *
hw=1280*960
i=ceil(log2(2048))
for n in range(10000,1,-1):
    hw = 1280 * 960
    i = ceil(log2(2048))
    pak=hw * i * n
    if pak / 96_468_992 <=132:
        print(n)
        break


