with open(r'./files/9778.txt') as file:
    data=[list(map(int,i.split())) for i in file]
pq=0
for line in data:
    pq+=1
    cnt=[line.count(i) for i in set(line)]
    pov=[i for i in line if line.count(i) >1]
    ne_pov=[i for i in line if line.count(i) ==1]
    if sorted(cnt) ==[1,1,1,1,2]:
        if pov[0] >= (sum(ne_pov)//4):
            print(pq)
            break
