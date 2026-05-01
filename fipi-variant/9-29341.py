with open(r'./9-29341') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    u1=max(line) < (sum(line) - max(line))
    if u1:
        if line[0]+line[1] != line[2] + line[3]:
            if line[0]+line[2] != line[1] + line[3]:
                if line[0] + line[3] != line[1] + line[2]:
                    cnt+=1
print(cnt)