with open(r'../files/24_18239.txt') as file:
    data = file.readline().strip()
k = -20000
a = data.split('-')
i = [i for i in range(len(a)) if a[i] == '']
data = [a[i[x] + 1:i[x + 1]] for x in range(len(i) - 1)]
data = [x for x in data if x]
ans = []
for b in data:
    l = s = 0
    ln = len(b[0])
    sum = int(b[0])
    for r in range(1, len(b)):
        s += int(b[r])
        sum = int(b[l]) - s
        ln += 1 + len(b[r])
        while sum <= k and l < r:
            ln -= len(b[l]) + 1
            s -= int(b[l + 1])
            l += 1
            if l <= r:
                sum = int(b[l]) - s
        if sum > k:
            ans.append(ln)

print(max(ans))
