with open(r'../files/24_17535.txt') as file:
    data=file.readline()
cnt=ans=dlina=l=0
for r in range(len(data)-1):
    if data[r:r+2]=='CD':
        cnt+=1
    if cnt==160:
        dlina=r-l+1
        ans = max(ans, dlina)
    while cnt>160:
        l+=1
        if data[l:l+2]=='CD':
            cnt-=1
        dlina=r-l+1
print(ans)




ans=0
data=data.replace('CD','C D')
data=data.split()
for i in range(len(data)-160):
    line=''.join(data[i:i+161])
    ans=max(ans,len(line))
print(ans)



with open(r'../files/24_17535.txt') as file:
    data=file.readline()
ans=cnt=l=r=0
len_data=len(data)
while r<len_data - 1:
    if cnt<=160:
        if data[r:r+2]=='CD':cnt+=1
        r+=1
    else:
        if data[l:l+2]=='CD':cnt-=1
        l+=1
    ans=max(ans,r-l)
print(ans)


