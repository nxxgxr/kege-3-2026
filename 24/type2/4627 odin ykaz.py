with open(r'../files/24_4627.txt') as file:
    data=file.readline()
cnt=ans=i=0
while i < len(data):
    if data[i:i+3] in 'NPO PNO':
        cnt+=1
        i+=3
    else:
        ans=max(ans,cnt)
        i+=1
        cnt=0
ans = max(ans, cnt)
print(ans)