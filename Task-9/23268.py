with open(r'./files/23268.txt') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    cnt+=1
    amount=[line.count(i) for i in set(line)]
    pov=[i for i in line if line.count(i)>1]
    ne_pov=[i for i in line if line.count(i)==1]
    if sorted(amount)==[1,1,1,2,2]:
        if sum(pov)/4 < max(ne_pov):
            print(cnt)
            break
