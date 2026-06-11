with open(r'../files/26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    obiem = [int(x) for x in file]
obiem = sorted(obiem)
cnt = last = 0
for i in obiem:
    if s - i >= 0:
        cnt += 1
        last = i
        s -= i
    else:
        s += last
        break
ans = 0
for i in obiem[::-1]:
    if s - i >= 0:
        ans = i
        break
print(cnt, ans)
