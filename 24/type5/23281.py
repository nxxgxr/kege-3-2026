

with open(r'../files/24_23281.txt') as file:
    data=file.readline()

ans=l=dlina=0
cnt_Y=cnt_2025=0
for r in range(len(data)-3):
    if data[r:r+4]=='2025':
        cnt_2025+=1
    if data[r]=='Y': cnt_Y+=1
    while cnt_Y>80:
        if data[l]=='Y': cnt_Y-=1
        l+=1
    if cnt_2025>=90 and cnt_Y==80:
        dlina=r-l+1
        ans=max(ans,dlina)
print(ans)