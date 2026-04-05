with open(r'./files/24347') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    minn=min(i for i in line)
    maxx=max(i for i in line)
    u1=line.count(maxx) == 1
    u2=(line[0] != minn and line[0] != maxx) and (line[-1] != minn and line[-1] != maxx)
    hapka=sorted(line)[-3:]
    u3=(hapka[0] * hapka[1] * hapka[2]) % minn ==0
    if u1 + u2 + u3 == 1:cnt+=1
print(cnt)