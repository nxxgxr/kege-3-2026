from math import *

def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, a) for a in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]


with open(r'./files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[0] == 'L' and data[1] == '3':
            stars += [list(map(float, [x, y]))]

kl1 = [dot for dot in dots if dot[1] > 10]
kl2 = [dot for dot in dots if dot[1] < 10]
cent1 = center(kl1)
cent2 = center(kl2)
A2 = max(dist(cent2, a) for a in stars) * 10_000 // 1
A1 = max(dist(cent1, a) for a in stars) * 10_000 // 1
print(A1, A2)

with open(r'./files/27_B_29080.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x,y,data = i.replace(',','.').split()
        dots+=[list(map(float,[x,y]))]
        if data[0]=='L':
            stars+=[list(map(float,[x,y]))]


kl1=[dot for dot in dots if dot[1]>22.5]
kl2=[dot for dot in dots if 16<dot[1]<22.5]
kl3=[dot for dot in dots if dot[1]<16]

cent1=center(kl1)#меньше всего
cent2=center(kl2)
cent3=center(kl3)# больше всего
# print(sum(1 for x in stars if x in kl1))
# print(sum(1 for x in stars if x in kl2))
# print(sum(1 for x in stars if x in kl3))
B1=dist(cent1,cent3)* 10_000 // 1
q=max(dist(a,b) for a in kl1 for b in kl2 if a in stars and b in stars)
w=max(dist(a,b) for a in kl1 for b in kl3 if a in stars and b in stars)
z=max(dist(a,b) for a in kl3 for b in kl2 if a in stars and b in stars)
B2=max(q,w,z)* 10_000 // 1

print(B1,B2)