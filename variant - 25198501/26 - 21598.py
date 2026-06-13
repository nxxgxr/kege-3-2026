with open(r'./files/26_21598.txt') as file:
    n=int(file.readline())
    times=[list(map(int,i.split())) for i in file]
time=[0]*(60*24+1)
for i in times:
    for x in range(i[0],i[1]+1):
        time[x]+=1

ans=[]
ans2=cnt=0
for i in range(1,len(time)-1):
    if time[i]==time[i+1] and time[i+1]!=0:
        cnt+=1
    elif time[i] != time[i+1]:
        ans+=[i]
        cnt=0
    ans2=max(ans2,cnt)
print(ans[-2],ans2)
