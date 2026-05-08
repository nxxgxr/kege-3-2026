#замена
from tabnanny import check

# with open(r'../files/24_9753.txt') as file:
#     data=file.readline()

# data=data.split('Y')
# ans=0
# for i in range(len(data)-150):
#     line='Y'.join(data[i:i+151])
#     ans=max(ans,len(line))
# print(ans)

#два указателя

with open(r'../files/24_9753.txt') as file:
    data=file.readline()

cnt=0
ans=0
dlina=0
l=0
for r in range(len(data)-1):
    if data[r]=='Y':
        cnt+=1
    if cnt==150:
        dlina=r-l+1
        ans = max(ans, dlina)
    while cnt>150:
        l+=1
        if data[l]=='Y':
            cnt-=1
        dlina=r-l+1
print(ans)


ans=cnt=l=r=0
while r<len(data):
    if cnt<=150:
        if data[r]=='Y':cnt+=1
        r+=1
    else:
        if data[l]=='Y':cnt-=1
        l+=1
    if l>0:
        ans=max(ans,r-l-1)
    else:
        ans=max(ans,r)
print(ans)