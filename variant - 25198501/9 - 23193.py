with open(r'./files/9.txt') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    cnt+=1
    amount=[line.count(i) for i in set(line)]
    pov=[x for x in line if line.count(x)==3]
    ne_pov=[x for x in line if line.count(x)==0]
    if sorted(amount)==[1,1,1,3]:
        if sum(pov)//3 > (sum(ne_pov))//3:
            print(cnt)
