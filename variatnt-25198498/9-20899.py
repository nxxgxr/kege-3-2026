
with open(r'./files/9.txt') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    maxx=max(line)
    u1=maxx< sum(line) - maxx
    pov=[x for x in line if line.count(x)>1]
    u2 = len(pov)==2
    if u1+u2==2:
        cnt+=1
        print(line)
print(cnt)
