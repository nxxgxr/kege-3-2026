with open(r'./files/26_21598.txt') as file:
    n=int(file.readline())
    times=[list(map(int,i.split())) for i in file]

time=[0]*60*24
for i in times:
    for x in range(i[0],i[1]+1):
        time[x]+=1
ans=[]
for i in range(len(time)-1):
    if time[i]!=time[i+1] and time[i+1]!=0:
        ans+=[i+1]

ans2=0
cnt=0

for x in range(len(time) - 1):
    if time[x]==time[x+1] and time[x]!=0:
        cnt+=1
        ans2=max(cnt,ans2)
    else:cnt=0
print(ans[-2],ans2)
