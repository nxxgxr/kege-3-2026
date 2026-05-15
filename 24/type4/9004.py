with open(r'../files/24-384.txt') as file:
    data = file.readline()
cnt = dlina = l = 0
ans = 10 ** 10
for r in range(len(data)):
    if data[r] == 'Z':
        cnt += 1
    while cnt >= 270:
        dlina = r - l + 1
        ans = min(ans, dlina)
        if data[l] == 'Z':
            cnt -= 1
        l += 1
print(ans)
