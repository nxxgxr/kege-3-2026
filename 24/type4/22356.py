from string import printable
with open(r'../files/24_22356.txt') as file:
    data = file.readline().lower()
alph = printable[:12]
l = ans = max_index=flag=r=0
n = len(data)
while r < n:
    if r < n and data[r] not in alph:
        r += 1
        continue
    start = r
    while r < n and data[r] in alph:
        r += 1
    j = start
    while j < r and data[j] == '0':
        j += 1
    if j == r:
        continue
    if data[r - 1] in '13579b':
        chislo = int(data[j:r], 12)
        if chislo > ans:
            ans = chislo
            max_index = j
print(max_index)