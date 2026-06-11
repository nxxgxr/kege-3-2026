with open(r'../files/26_9847.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]
times = sorted(times)
time = [0] * 1440
for i in times:
    for x in range(i[0], i[1]):
        time[x] += 1
l = dlina = 0
for r in range(len(time) - 1):
    if time[r] == time[r + 1] and time[r] > 0:
        dlina = r - l + 1
        if time[r] == max(time) and len(time[l:r + 1]) > 1:
            print(dlina, time[r])
    if time[r] != time[r + 1]: l = r + 1
