from math import *

def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, A) for A in cl)
        res += [[sum_dist, dot]]
    return min(res)[1]

with open(r'./files/27_A_29077.txt') as file:
    stars = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[0] == 'N' and data[1] == '9' and data[2]=='I':
            stars += [list(map(float, [x, y]))]

kl1 = [dot for dot in dots if dot[1] > 10]
kl2 = [dot for dot in dots if dot[1] < 10]
center1=center(kl1)
center2=center(kl2)


A1=min(dist(kl,A) for A in stars for kl in (center1,center2))*10_000 //1
A2=max(dist(kl,A) for A in stars for kl in (center1,center2))*10_000 //1


print(A1,A2)


with (open(r'./files/27_B_29077.txt') as file):
    stars1 = []
    stars2 = []
    dots = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[1] in '0123456789':
            if int(data[1])> 7:
                stars1 += [list(map(float, [x, y]))]
        if data[1] in '0123456789':
            if int(data[1])<4:
                stars2 += [list(map(float, [x, y]))]

kl1=[dot for dot in dots if dot[1]>22.5]
kl2=[dot for dot in dots if 15<dot[1]<22.5]
kl3=[dot for dot in dots if dot[1]<15]

center1=center(kl1)
center2=center(kl2)
center3=center(kl3)

# print(len(kl1),len(kl2),len(kl3))

B1=sum(1 for x in kl3 if x in stars1) //1
B2=sum(1 for x in kl2 if x in stars2) //1
print(B1,B2)
