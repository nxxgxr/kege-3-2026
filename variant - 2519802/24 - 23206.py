from string import printable

alph = printable[:10]

with open('./files/24_23206.txt') as file:
    data = file.readline()

cnt_S = dlina = l = 0
ans = 0
flag = 0
cifr = 0

for r in range(len(data)):
    if data[r] == 'S':
        cnt_S += 1
    if data[r] in '02468':
        if flag == 0:
            cifr = data[r]
            l = r
            flag = 1
            cnt_S = 0
        else:
            cifr = data[r]
            l = r
            cnt_S = 0
    while cnt_S > 35:
        if data[l] == 'S':
            cnt_S -= 1
        l += 1
    if cnt_S == 35:
        dlina = r - l + 1
        ans = max(ans, dlina)

print(ans)
