with open(r'../files/26_24.txt') as file:
    s, n = map(int,file.readline().split())
    obiem = [int(x) for x in file]
obiem = sorted(obiem)
cnt = last = 0
for x in obiem:
    if s - x >= 0:
        s-= x
        cnt += 1
        ostatok = s + x
last = 0
for i in obiem:
    if i <= ostatok:last = i
    else:break
print(cnt, last)