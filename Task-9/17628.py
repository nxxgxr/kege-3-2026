with open(r'./files/17628') as file:
    data=[list(map(int,i.split())) for i in file]
cnt=0
for line in data:
    mx=max(line)
    mn=min(line)
    if mn+mx<=sum(line) - mn -mx:
        cnt+=1

print(cnt)