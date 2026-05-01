with open(r'../files/24_1975.txt') as file:
    data = file.readline()

cnt=1
max_cnt=0
for i in range(len(data)-1):
    cnt+=1
    if data[i]=='P' and data[i+1]=='P':
        cnt=1
    if cnt>max_cnt:
        max_cnt=cnt
print(max_cnt)