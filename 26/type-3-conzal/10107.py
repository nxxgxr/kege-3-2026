with open(r'../files/26_10107.txt') as file:
    n=int(file.readline())
    times=[list(map(int,i.split())) for i in file]

times=sorted(times,key=lambda x: x[1])
cnt=1
last=[times[0]]
for i in times:
    if i[0]>=last[-1][1]:
        cnt+=1
        last+=[i]
    else:
        continue
ans=0
for i in sorted(times)[::-1]:
    if i[0]>last[-2][0]:
        ans=i[0]
        break

print(len(last),ans-last[-2][1])

