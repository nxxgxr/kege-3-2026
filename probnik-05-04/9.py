with open(r'./9.txt') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    cnt+=1
    amount=[line.count(i) for i in set(line)]
    pov=[i for i in line if line.count(i)>1]
    ne_pov=[i for i in line if line.count(i)==1]
    if sorted(amount)==[1,1,1,1,2]:
        if pov[0] >= (sum(ne_pov))/4:
            print(cnt)
            break
