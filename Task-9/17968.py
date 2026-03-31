with open(r'./files/17968.txt') as file:
    data=[list(map(int,i.split())) for i in file]

cnt=0
for line in data:
    if max(line)  < sum(line) - max(line):
        chet=sum(i for i in line if i%2==0)
        nechet=sum(i for i in line if i%2==1)
        if chet==nechet:
            cnt+=1


print(cnt)

