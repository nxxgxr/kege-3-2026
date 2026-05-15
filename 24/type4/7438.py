with open(r'../files/24-293.txt') as file:
    data = file.readline()
from string import printable

ans = dlina = l = cnt = 0
for r in range(len(data) - 1):
    if data[r] == 'D':
        cnt += 1
    if data[r] in printable[:10]:
        cnt = 0
        l = r + 1
        continue
    if data[r:r + 2] in 'DS SD':
        cnt = 0
        l = r + 2
        continue
    while cnt > 100:
        if data[l] == 'D':
            cnt -= 1
        l += 1
    if cnt == 100:
        dlina = r - l + 1
        ans = max(ans, dlina)

print(ans)
