with open(r'../files/24_18239.txt') as file:
    data = file.readline().strip()
alph = '123456789'
dlina = l = ans = 0
cnt = 0

for r in range(1, len(data) - 1):
    while l < len(data) and data[l] == '-':
        l += 1
    if r + 1 < len(data) and data[r] == '-' and data[r + 1] == '-':
        l = r + 2
        cnt = 0
        continue
    if r + 1 < len(data) and data[r] == '-' and data[r + 1] in alph:
        if r > l and data[l] != '-':
            cnt = eval(data[l:r])
    while cnt < -20000 and l < r:
        l += 1
        while l < len(data) and data[l] == '-':
            l += 1
        if r > l and data[l] != '-':
            cnt = eval(data[l:r])
    if cnt > -20000 and data[l] != '-':
        dlina = r - l + 1
        ans = max(ans, dlina)

    print(ans)
print(ans)
