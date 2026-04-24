from math import *
def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,d) for d in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_B_29074.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[0]=='L' and data[2:]=='V':
            stars+=[list(map(float,[x,y]))]

kl1=[d for d in dots if d[1]>22.5]
kl2=[d for d in dots if 16<d[1]<22.5]
kl3=[d for d in dots if d[1]<16]
cent1=center(kl1)
cent2=center(kl2)
cent3=center(kl3)

q1=[dist(cent1,b)  for b in kl1 if b in stars]
q2=[dist(cent2,b)  for b in kl2 if b in stars]
q3=[dist(cent3,b)  for b in kl3 if b in stars]

print(min(q2)*10_000)
print(max(q3)*10_000)
