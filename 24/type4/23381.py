from string import printable

with open(r'../files/24_23381.txt') as file:
    data = file.readline()
alph = printable[36:62]
cifr = printable[:10:2]
ans = dlina = cnt = flag = 0
for r in range(len(data) - 1):
    if data[r] in cifr and data[r + 1] in alph:
        cnt += 1
        flag = 1
    elif data[r] in alph and data[r] == data[r + 1] and flag == 1:
        cnt += 1
    elif flag == 1 and data[r] in alph and data[r + 1] in cifr:
        cnt += 1
        ans = max(ans, cnt)
        cnt = 0
    else:
        ans = max(ans, cnt)
print(ans)
