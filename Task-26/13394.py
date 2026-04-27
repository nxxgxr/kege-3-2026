from math import *
with open(r'./files/26.6_13394.txt') as file:
    n=int(file.readline())
    data=[int(x) for x in file]
product=sorted(data)
cnt=0
for i in product:
    cnt+=1
    if i>350:
        break
neych=sum(product[:cnt-1])
ych=[x for x in product if x not in product[:cnt-1]]

odnim=ceil(sum(product) - (sum(i for i in ych[:len(ych)//3] if i>350))*0.75 )

razn=neych
for i in range(0,len(ych)-2,3):
    razn+=ceil(ych[i]*0.25 +ych[i+1] + ych[i+2])
print(razn,odnim)