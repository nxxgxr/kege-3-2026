from math import *
def cent(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,A) for A in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_23284.txt') as file:
    dots=[list(map(float,i.replace(',','.').split())) for i in file]

kl1=[dot for dot in dots if dot[1]>15]
kl2=[dot for dot in dots if dot[1]<15]
cent1=cent(kl1)
cent2=cent(kl2)

Px=(cent1[0]+cent2[0])*10_000//1
Py=(cent1[1]+cent2[1])*10_000//1
print(Px,Py)


with open(r'./file/27_B_23284.txt') as file:
    dots2=[list(map(float,i.replace(',','.').split())) for i in file]

kl1=[dot for dot in dots2 if 4<dot[0]<11 and 23<dot[1]<30]
kl2=[dot for dot in dots2 if 13<dot[0]<19 and 29<dot[1]<35]
kl3=[dot for dot in dots2 if 19<dot[0]<24 and 26<dot[1]<32]


cent1=cent(kl1)
cent2=cent(kl2)
cent3=cent(kl3)

# print(dist(cent1,cent2),dist(cent1,cent3),dist(cent3,cent2))
Q1=dist(cent3,cent2)*10_000 //1
Q2=dist(cent3,cent1)*10_000 //1
print(Q1,Q2)