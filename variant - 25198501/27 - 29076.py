from math import *

def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,A) for A in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./files/27_A_29076.txt') as file:
    stars=[]
    dots=[]
    for line in file:
        x,y,data=line.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[1]=='2':
            stars+=[list(map(float,[x,y]))]

kl1=[dot for dot in dots if dot[1]>10]
kl2=[dot for dot in dots if dot[1]<10]
center1=center(kl1)
center2=center(kl2)
# x=sum(1 for x in kl1 if x in stars)
# y=sum(1 for x in kl2 if x in stars)
A1=int(center1[0] * 10_000)
A2=int(center2[1] * 10_000)
print(A1,A2)

with open(r'./files/27_B_29076.txt') as file:
    stars=[]
    dots=[]
    for line in file:
        x,y,data=line.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[0]=='Y':
            stars+=[list(map(float,[x,y]))]
kl1=[dot for dot in dots if dot[1]>22.5]
kl2=[dot for dot in dots if 15<dot[1]<22.5]
kl3=[dot for dot in dots if dot[1]<15]
center1=center(kl1)
center2=center(kl2)
center3=center(kl3)
# q=sum(1 for x in kl1 if x in stars)
# w=sum(1 for x in kl2 if x in stars)
# e=sum(1 for x in kl3 if x in stars)
# print(q,w,e)
B1=int(dist(center2,center3)* 10_000)
B2=int(max(dist(center(kl),A) for kl in (kl1,kl2,kl3) for A in stars if A in kl) * 10_000)
print(B1,B2)
