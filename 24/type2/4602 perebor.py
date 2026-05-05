with open(r'../files/24_4602.txt') as file:
    data=file.readline()
cnt=0
ans=0
for i in range(len(data)-1):
    if data[i] in 'BCD' and data[i+1] in 'AO':
        for x in range(i,len(data)-1,2):
            if data[x] in 'BCD' and data[x + 1] in 'AO':
                cnt+=1
            else:
                ans=max(ans,cnt)
                cnt=0
                break
        ans=max(ans,cnt)
print(ans)