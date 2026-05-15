with open(r'../files/24_17535.txt') as file:
    data = file.readline()
ans = cnt = l = dlina = 0
for r in range(len(data) - 1):
    if data[r:r + 2] in 'CD':
        cnt += 1
    while cnt > 160:
        l += 1
        if data[l:l + 2] == 'CD':
            cnt -= 1
    if cnt == 160:
        dlina = r - l + 1
        ans = max(ans, dlina)
print(ans)
