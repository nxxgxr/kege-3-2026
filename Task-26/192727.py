with open(r'./files/26.2_19727.txt') as file:
    m,n=map(int,file.readline().split())
    moloko=[int(x) for x in file]
moloko=sorted(moloko)
ans=[]
cnt=0
for i in moloko:
    if sum(ans)+i <=m:
        ans+=[i]
    else:
        break
moloko=sorted(moloko,reverse=True)
ans=ans[:-1]
cnt=0
for i in moloko:
    if sum(ans)+i <=m:
        cnt+=1
print(len(ans),n-cnt)