with open(r'./files/9.txt') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    amount=[line.count(i) for i in set(line)]
    pov=[x for x in line if line.count(x)>1]
    ne_pov=[x for x in line if line.count(x)==1]
    if sorted(amount)==[1,2,2,2]:
        if (min(pov) + max(pov))/2 < sum(ne_pov):
            cnt+=1
print(cnt)
