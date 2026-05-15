with open(r'../files/24_10105.txt') as file:
    data = file.readline()
ans = l = cnt = dlina = 0
alph = 'UVWXYZ'
for r in range(len(data) - 1):
    if data[r] == 'T':
        cnt += 1
    while cnt > 100:
        l += 1
        if data[l] == 'T':
            cnt -= 1
    if cnt == 100:
        dlina = r - l + 1
        ans = max(ans, dlina)
print(ans)
