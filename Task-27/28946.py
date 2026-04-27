from math import *


def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, A) for A in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]


with open(r'./file/27_A_28946.txt') as file:
    dot = [list(map(float, i.replace(',', '.').split())) for i in file]

kl1 = [x for x in dot if x[1] > 15]
kl2 = [x for x in dot if x[1] < 15]
cent1 = center(kl1)
cent2 = center(kl2)

A1 = len([x for x in kl1 if x[1] < cent1[1]])
A2 = abs(cent2[0] - cent1[0]) * 10_000 // 1
print(A1, A2)

with open(r'./file/27_B_28946.txt') as file:
    dot2 = [list(map(float, i.replace(',', '.').split())) for i in file]

kl1b=[x for x in dot2 if x[1]>22.5]
kl2b=[x for x in dot2 if x[1]<22.5 and x[0]<24]
kl3b=[x for x in dot2 if x[1]<22.5 and x[0]>24]
cent1b=center(kl1b)
cent2b=center(kl2b)
cent3b=center(kl3b)

B1=len([x for x in kl3b if (cent3b[0]-0.9 < x[0] < cent3b[0]+0.9)  and (cent3b[1]-0.9 < x[1] < cent3b[1]+0.9)])
B2=abs(cent1b[1]-cent2b[1])*10_000//1

print(B1,B2)