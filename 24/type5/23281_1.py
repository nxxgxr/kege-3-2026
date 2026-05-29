with open(r'../files/24_23281.txt') as file:
    data=file.readline()

dlina=l=ans=cnt=0
cnt_2025=0
for r in range(len(data)-1):
    if data[r:r+4]=='2025':
        cnt_2025+=1
    if data[r]=='Y':
        cnt+=1
    while cnt>80:
        if data[l]=='Y':
            cnt-=1
        l+=1
    if cnt==80 and cnt_2025>=90:
        dlina=r-l+1
        ans=max(ans,dlina)
print(ans)