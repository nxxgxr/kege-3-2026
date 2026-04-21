from math import *
def krai(cl):
    res=[]
    for dot in cl:
        sum_dist=sum(dist(dot,A) for A in cl)
        res+=[[sum_dist,dot]]
    return max(res)[1]

with open(r'./file/27.17.A_19566.txt') as file:
    dots=[list(map(float,i.replace(',','.').split())) for i in file]


kl1a=[dot for dot in dots if (-2 < dot[1] < -4 and -1.5 < dot[0] < 3) or dot[1]<-4]
kl2a=[dot for dot in dots if (dot[1] < 0 and 5.5< dot[0] < 14) or (dot[1]>0 and 8 < dot[0] <12)]

krai1a=krai(kl1a)
krai2a=krai(kl2a)
print('27a')
print((krai1a[0]+krai2a[0])/2 * 10000//1)
print(abs(krai1a[1]+krai2a[1])/2 * 10000//1)

with open(r'./file/27.17.B_19566.txt') as file:
    dots2 = [list(map(float, i.replace(',', '.').split())) for i in file]


eps=1
clusters=[]
while dots2:
    cluster = [dots2.pop()]
    for dot in cluster:
        for d in dots2.copy():
            if dist(dot,d) < eps:
                cluster+=[d]
                dots2.remove(d)
    if len(cluster)>4:
        clusters+=[cluster]
print([len(cluster) for cluster in clusters])

# kl1b=[dot for dot in dots2 if (dot[1]<-4) or (-4<dot[1]<0 and (-16<dot[0]<6)) or (0<dot[1]<4 and -10<dot[0]<2)]
# kl2b=[dot for dot in dots2 if (9<dot[1]<18 and -12.5<dot[0]<13.2) or (18<dot[1]<23 and -6<dot[0]<9)]
# kl3b=[dot for dot in dots2 if (16<dot[1] and dot[0]>13)]
# kl4b=[dot for dot in dots if (-4<dot[1]<9.6) and dot[0]>6]
# krai1b=krai(kl1b)
# krai2b=krai(kl2b)
# krai3b=krai(kl3b)
# krai4b=krai(kl4b)

