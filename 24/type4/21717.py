with open(r'../files/24_21717.txt') as file:
    data = file.readline()
dlina = l = cnt = 0
ans=1000
for r in range(len(data) - 2):
    if data[r:r + 3] == 'RSQ':
        cnt += 1
    while cnt > 130:
        if data[l:l + 3] == 'RSQ':
            cnt -= 1
            l+=2
        l+=1
    if cnt == 130:
        strok=data[l:r+3]
        Lindex=strok.find('R')
        Rindex=strok.rfind('Q') + 1
        dlina = Rindex - Lindex + 1
        ans = min(ans, dlina)
print(ans)
