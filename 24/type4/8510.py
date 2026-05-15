with open(r'../files/24_8510.txt') as file:
    data=file.readline()
cnt=ans=1
for i in range(len(data)-1):
    if data[i] in 'NOP' and data[i+1] in 'NOP':
        ans = max(ans, cnt)
        cnt = 1
    else:cnt+=1
print(ans)