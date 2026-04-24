from math import *

def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,A) for A in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_28766.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[0] == 'Y' and data[2:]=='III':
            stars+=[list(map(float,[x,y]))]
kl1=[dot for dot in dots if dot[1]>8]
kl2=[dot for dot in dots if dot[1]<8]

center1=center(kl1)
center2=center(kl1)

maxkl=max(center2,center1, key=len)
minkl=min(center2,center1, key=len)

print(min(dist(minkl,x) for x in stars)*10000)
print(max(dist(minkl,x) for x in stars)*10000)
