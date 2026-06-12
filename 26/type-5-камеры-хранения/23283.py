with open(r'../files/26_23283.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
times = sorted(times)
okno = [0] * k
cnt = 0
max_first = []
for i in times:
    for x in range(k):
        if okno[x] < i[0]:
            max_first += [x+1]
            okno[x] = i[1]
            cnt += 1
            break
print(cnt,max_first[-1])
