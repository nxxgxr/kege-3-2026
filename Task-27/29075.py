from math import *


def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, A) for A in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]


with open(r'./file/27_A_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[-3:] == 'III':
            stars += [list(map(float, [x, y]))]

kl1 = [x for x in dots if x[1] > 10]
kl2 = [x for x in dots if x[1] < 10]
cent1 = center(kl1)
cent2 = center(kl2)
t = [1 for i in kl1 if i in stars]
t2 = [1 for i in kl2 if i in stars]
# print(len(t), len(t2))

A1 = cent1[0] * 10_000 // 1
A2 = cent2[1] * 10_000 // 1
print(A1, A2)

with open(r'./file/27_B_29075.txt') as file:
    dots2 = []
    stars2 = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots2 += [list(map(float, [x, y]))]
        if data[0] == 'J':
            stars2 += [list(map(float, [x, y]))]

kl1b = [x for x in dots2 if x[1] > 22]
kl2b = [x for x in dots2 if 16 < x[1] < 22]
kl3b = [x for x in dots2 if 16 > x[1]]

B1 = min([dist(a, b) for a in (kl1b + kl2b + kl3b) for b in (kl1b + kl2b + kl3b) if
          a in stars2 and b in stars2 and not ((a in kl1b and b in kl1b) or (a in kl2b and b in kl2b) or (
                  a in kl3b and b in kl3b))]) * 10_000 // 1
B2 = max([dist(a, b) for a in (kl1b + kl2b + kl3b) for b in (kl1b + kl2b + kl3b) if
          a in stars2 and b in stars2 and not ((a in kl1b and b in kl1b) or (a in kl2b and b in kl2b) or (
                  a in kl3b and b in kl3b))]) * 10_000 // 1
print(B1, B2)
