from math import *

def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,b) for b in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_23209.txt') as file:
    dots=[list(map(float,i.replace(',','.').split())) for i in file]
kl1=[dot for dot in dots if dot[0] < 5]
kl2=[dot for dot in dots if dot[0] > 5]
cent1a=center(kl1)
cent2a=center(kl2)
print('27a Px:', max(cent1a[0],cent2a[0])*10000)
print('27a Py:', max(cent1a[1],cent2a[1])*10000)

with open(r'./file/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

kl1b=[dot for dot in dots if 4<dot[1]<11]
kl2b=[dot for dot in dots if 16<dot[1]<21]
kl3b=[dot for dot in dots if 21<dot[1]<26]

center1b=center(kl1b)
center2b=center(kl2b)
center3b=center(kl3b)
print(len(kl1b),len(kl2b),len(kl3b))
maxx=center(max([len(kl),kl] for kl in (kl1b,kl2b,kl3b))[1])
minn=center(min([len(kl),kl] for kl in (kl1b,kl2b,kl3b))[1])

print('27b Qx:', (maxx[0] - minn[0])*10000)
print('27b Qx:', abs(maxx[1] - minn[1])*10000)
