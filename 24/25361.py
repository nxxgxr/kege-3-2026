with open('24_25361.txt') as file:
    data = file.readline()
ans=0
for i in range(len(data)):
    if data[i] in '02468':
        cnt_f = 0
        cnt = 1
        for j in range(i +1 , len(data)):
            if data[j] == 'F':
                cnt_f += 1
            if data[j] in '02468' or cnt_f == 77:
                break
            cnt += 1
        if cnt_f==77:
            ans=max(ans,cnt)

print(ans)
