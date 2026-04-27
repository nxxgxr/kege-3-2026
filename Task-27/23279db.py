from math import *

def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,b) for b in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_23209.txt') as file:
    dots=[list(map(float,i.replace(',','.').split())) for i in file]
eps=1
klaster=[]
while dots:
    kl=[dots.pop()]
    for dot in kl:
        for d in dots.copy():
            if dist(dot,d) < eps:
                kl+=[d]
                dots.remove(d)
    klaster+=[kl]
print([len(kl) for kl in klaster])


centers=[center(kl) for kl in klaster]
print(max(a for a in centers)[0] * 10000)
print(max(a for a in centers)[1] * 10000)

with open(r'./file/27_B_23209.txt') as file:
    dots=[list(map(float,i.replace(',','.').split())) for i in file]

eps=2
klasters2=[]
while dots:
    kl1 = [dots.pop()]
    for dot in kl1:
        for d in dots.copy():
            if dist(dot, d) < eps:
                kl1 += [d]
                dots.remove(d)
    if len(kl1)>1:
        klasters2 += [kl1]
centers=[center(kl) for kl in klasters2]

max_x=max(centers)[0]
max_y=max(centers)[1]
min_x=min(centers)[0]
min_y=min(centers)[1]
print((max_x - min_x)*10000)
print((max_y - min_y)*10000)
