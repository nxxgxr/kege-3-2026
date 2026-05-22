with open(r'../files/24-295.txt') as file:
    data = file.readline()

ans = cnt = dlina = l = 0

for r in range(len(data) - 1):

    if data[r:r + 2] == 'DE':
        cnt += 1
    while cnt > 240:
        if data[l:l + 2] == 'DE':
            cnt -= 1
        l += 1
    dlina = r - l + 2
    ans = max(ans, dlina)
print(ans)
