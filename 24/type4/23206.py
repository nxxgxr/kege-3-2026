#re
# from re import finditer
# with open(r'../files/24_23206.txt') as file:
#     data=file.readline()
#
# pattern=r'[02468]([^02468S]*S){35}[^02468S]*'
# q=[x.group() for x in finditer(pattern,data)]
# print(len(max(q,key=len)))

#zamena

with open(r'../files/24_23206.txt') as file:
    data=file.readline()
ans=l=dlina=cnt=cntS=0
for r in range(len(data)):
    if cnt==0 and data[r] in '02468':
        cnt+=1
    if cnt>0 and data[r]  in '02468':
        dlina=cnt=cntS=0
        l=r
    if data[r]=='S':
        cntS+=1
    if cntS==35:
        dlina=r-l+1
        ans=max(ans,dlina)
    while cntS>35:
        l+=1
        if data[l]=='S':
            cntS-=1
        dlina=r-l+1
print(ans)
