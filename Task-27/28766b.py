from math import *

def center(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, A) for A in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]

with open(r'./file/27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots += [list(map(float, [x, y]))]
        if data[0] == 'Z' and data[2:] == 'I':
            stars += [list(map(float, [x, y]))]
kl1 = [d for d in dots if d[1] > 22.5]
kl2 = [d for d in dots if 15 < d[1] < 22.5]
kl3 = [d for d in dots if d[1] < 15]
q1 = (dist(A, B) for A in kl1 for B in kl1 if A in stars and B in stars and dist(A, B) > 0)
q2 = (dist(A, B) for A in kl2 for B in kl2 if A in stars and B in stars and dist(A, B) > 0)
q3 = (dist(A, B) for A in kl3 for B in kl3 if A in stars and B in stars and dist(A, B) > 0)
print(min(q3) * 10_000)
cnt1 = cnt2 = cnt3 = 0
for i in stars:
    if i in kl1: cnt1 += 1
    if i in kl2: cnt2 += 1
    if i in kl3: cnt3 += 1
print(cnt1, cnt2, cnt3)
print(dist(center(kl2), center(kl3)) * 10_000)
