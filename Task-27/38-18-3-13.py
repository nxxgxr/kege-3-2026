cl1, cl2, cl3 = [], [], []

for i in open('./file/27_1B.txt'):
    x, y = [float(j) for j in i.split()]
    if y < 4: cl1.append([x, y])
    if 4 < y < 7: cl2.append([x, y])
    if y > 7: cl3.append([x, y])

from math import *
def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append([s, p1])
    return min(mn)[1]

x1, y1 = center(cl1)
x2, y2 = center(cl2)
x3, y3 = center(cl3)
Px = (x1 + x2 + x3) / 3
Py = (y1 + y2 + y3) / 3

print(int(Px * 10_000), int(Py * 10_000))