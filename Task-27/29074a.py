from math import *
def center(kl):
    res=[]
    for dot in kl:
        sum_dist=sum(dist(dot,d) for d in kl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_29074.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data=i.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[0]=='Z':
            stars+=[list(map(float,[x,y]))]
kl1=[d for d in dots if d[1]>10]
kl2=[d for d in dots if d[1]<10]
cnt1=cnt2=0
for i in stars:
    if i in kl1:cnt1+=1
    if i in kl2:cnt2+=1
print(min(cnt1,cnt2))
print(max(cnt1,cnt2))