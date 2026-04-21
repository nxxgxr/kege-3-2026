from math import *
def center(cl):
    res=[]
    for dot in cl:
        sum_dist=sum(dist(dot,A) for A in cl)
        res+=[[sum_dist,dot]]
    return min(res)[1]

with open(r'./file/27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

kl1 = [dot for dot in dots if (dot[1] > (5 / 6 * dot[0] - 10))]
kl2 = [dot for dot in dots if (dot[1] < (5 / 6 * dot[0] - 10)) and dot[1] > -6]
kl3 = [dot for dot in dots if dot[1] < -6]
center1a=center(kl1)
center2a=center(kl2)
center3a=center(kl3)

print((center1a[0]+center2a[0]+center3a[0])/3 * 10000//1)
print(abs(center1a[1]+center2a[1]+center3a[1])/3 * 10000//1)


with open(r'./file/27_B_21599.txt') as file:
    dots2 = [list(map(float, i.replace(',', '.').split())) for i in file]

kl1b=[dot for dot in dots2 if dot[1] < (-19/12 * dot[0] - 19)]
kl2b=[dot for dot in dots2 if (dot[1] > (-19/12 * dot[0] - 19)) and (dot[0] < -10)]
kl3b=[dot for dot in dots2 if (dot[0] > -10 ) and (dot[1]> (10/7 * dot[0] + 10))]
kl4b=[dot for dot in dots2 if (dot[1]< (10/7 * dot[0] + 10)) and (dot[1] > dot[0])]
kl5b=[dot for dot in dots2 if (dot[1] < dot[0]) and dot[1]>-5]
kl6b=[dot for dot in dots2 if  dot[1]<-5]
center1b=center(kl1b)
center2b=center(kl2b)
center3b=center(kl3b)
center4b=center(kl4b)
center5b=center(kl5b)
center6b=center(kl6b)

print(abs(center1b[0]+center2b[0]+center3b[0]+center4b[0]+center5b[0]+center6b[0])/6 * 10000//1)
print(abs(center1b[1]+center2b[1]+center3b[1]+center4b[1]+center5b[1]+center6b[1])/6 * 10000//1)
