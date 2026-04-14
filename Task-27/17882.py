from math import *
def cent(kl):
    res = []
    for dot in kl:
        sum_dist = sum(dist(dot, d) for d in kl)
        res += [[sum_dist, dot]]
    return min(res)[1]
with open(r'file/27_A_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]
kl1a = [dot for dot in dots if dot[0] < 1]
kl2a = [dot for dot in dots if dot[0] > 1]
center1a = cent(kl1a)
center2a = cent(kl2a)
print('27a Px:', (center1a[0] + center2a[0]) / 2 * 10_000 // 1)
print('27a Py:', (center1a[1] + center2a[1]) / 2 * 10_000 // 1)


with open(r'file/27_B_17882.txt') as file:
    dots2=[list(map(float, i.split())) for i in file]
kl1b=[dot for dot in dots2 if dot[1]>7]
kl2b=[dot for dot in dots2 if dot[0]>5]
kl3b=[dot for dot in dots2 if dot[1]<3]
center1b=(cent(kl1b))
center2b=(cent(kl2b))
center3b=(cent(kl3b))

print('27б Px:', (center1b[0] + center2b[0] + center3b[0]) / 3 * 10_000 // 1)
print('27б Py:', (center1b[1] + center2b[1] + center3b[1]) / 3 * 10_000 // 1)