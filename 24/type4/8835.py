with open(r'../files/24-371.txt') as file:
    data = file.readline()

ans = cnt = dlina = l = 0

for r in range(len(data)):
    if data[r] == 'M':
        cnt += 1
    if data[r] == '.':
        if cnt == 112:
            dlina = r - l + 1
            ans = max(ans, dlina)
        cnt = 0
        l = r + 1
    while cnt > 112:
        if data[l] == 'M':
            cnt -= 1
        l += 1
print(ans)
