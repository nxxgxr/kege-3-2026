with open(r'./files/9740.txt') as file:
    data=[list(map(int,i.split())) for i in file]
ct=0
for line in data:
    pov=[i for i in line if line.count(i)>1]
    ne_pov=[i for i in line if line.count(i)==1]
    cnt=[line.count(i) for i in set(line)]
    if sorted(cnt) == [1,1,1,1,3]:
        if pov[0] >= (sum(ne_pov)/4):
            ct+=1
print(ct)