with open(r'./files/26.2_19727.txt') as file:
    m,n=map(int,file.readline().split())
    ves=[int(x) for x in file]

ves=sorted(ves)
cnt=0
ans=[]
summ=m
for i in ves:
    if summ-i>0:
        cnt+=1
        summ-=i
        ans+=[i]
ans=ans[:-1]
summ=sum(ans)
ans2=0
for i in ves[ves.index(ans[-1])+1:]:
    if m-summ-i<0:
        ans2+=1
print(cnt,ans2)