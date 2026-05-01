from math import *


def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, A) for A in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]


with open(r'./27_A_29357.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[0] == 'M' and data[-3:] == 'III':
            stars += [list(map(float, [x, y]))]

kl1 = [x for x in dots if x[1] > 15]
kl2 = [x for x in dots if x[1] < 15]
cent1 = center(kl1)
cent2 = center(kl2)
# print(len(kl1), len(kl2))

Ax = min((dist(A, cent2), A) for A in stars)[1][0] * 10_000 // 1
Ay = min((dist(A, cent2), A) for A in stars)[1][1] * 10_000 // 1
print(Ax, Ay)

with open(r'./27_B_29357.txt') as file:
    dots = []
    stars = []
    stars2 = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[0] == 'K' and data[-3:] == 'III':
            stars += [list(map(float, [x, y]))]
        if data[0] == 'G' and data[-1] == 'V' and data[-2:] != 'IV':
            stars2 += [list(map(float, [x, y]))]

kl1b = [x for x in dots if x[1] < 30]
kl2b = [x for x in dots if x[1] > 30 and x[0] < 16]
kl3b = [x for x in dots if x[1] > 30 and x[0] > 16]

cent1b = center(kl1b)
cent2b = center(kl2b)
cent3b = center(kl3b)

q1 = [1 for x in kl1b if x in stars]
q2 = [1 for x in kl2b if x in stars]
q3 = [1 for x in kl3b if x in stars]
# print(len(q1),len(q2),len(q3))
B1 = dist(cent1b, cent3b) * 10_000 // 1

w1 = max(dist(a, b) for a in kl1b for b in kl1b if a in stars2 if b in stars2)
w2 = max(dist(a, b) for a in kl2b for b in kl2b if a in stars2 if b in stars2)
w3 = max(dist(a, b) for a in kl3b for b in kl3b if a in stars2 if b in stars2)
B2 = max(w1, w2, w3) * 10_000 // 1
# print(w1, w2, w3)
print(B1, B2)
