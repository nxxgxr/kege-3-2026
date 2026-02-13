from math import *
#1855
l=101
n=10 + 4090
i=ceil(log2(n)) #bit
I= ceil(l * i /8)#byte
print(I*2048/2**10)

#23270
for l in range(1,10**9):
    n=10+27
    i=ceil(log2(n)) #bit
    I= ceil(l * i /8)#byte
    if 3548 * I > 12*2**10:
        print(l)
        break

for n in range(1,10**9):
    i=ceil(log2(n))
    l=172
    I=ceil(l*i/8)
    if I*356984 >= 54 * 2 **20:
        print(n)
        break