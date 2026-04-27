from math import *


def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, A) for A in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]


with open(r'./file/27_A_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[1] == '2':
            stars += [list(map(float, [x, y]))]
kl1 = [x for x in dots if x[1] > 10]
kl2 = [x for x in dots if x[1] < 10]
cent1 = center(kl1)
cent2 = center(kl2)
p = [1 for i in kl1 if i in stars]
q = [1 for i in stars if i in kl2]
# print(len(p),len(q))
print(cent1[0] * 10_000 // 1, cent2[1] * 10_000 // 1)

with open(r'./file/27_B_29076.txt') as file:
    dots2 = []
    stars2 = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots2 += [list(map(float, [x, y]))]
        if data[0] == 'Y':
            stars2 += [list(map(float, [x, y]))]

kl1b = [x for x in dots2 if x[1] > 22]
kl2b = [x for x in dots2 if 16 < x[1] < 22]
kl3b = [x for x in dots2 if 16 > x[1]]

cent1b = center(kl1b)
cent2b = center(kl2b)
cent3b = center(kl3b)
o = [1 for i in kl1b if i in stars2]
i = [1 for i in kl2b if i in stars2]
u = [1 for i in kl3b if i in stars2]
# print(len(o),len(i),len(u))
B1 = dist(cent2b, cent3b) * 10_000

y = max([dist(cent1b, x) for x in kl1b if x in stars2])
y2 = max([dist(cent2b, x) for x in kl2b if x in stars2])
y3 = max([dist(cent3b, x) for x in kl3b if x in stars2])
print(B1 // 1, y3 * 10_000 // 1)
