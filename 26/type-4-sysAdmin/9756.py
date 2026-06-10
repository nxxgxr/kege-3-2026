with open(r'../files/26_9756.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

events = sorted(times, key=lambda x: (x[1], x[0]))
approved = [events[0]]

for i in events:
    if i[0] >= approved[-1][1]:
        approved += [i]

approved = approved[:-1]

for i in events[::-1]:
    if approved[-1][1] <= i[0]:
        approved += [i]
        break
print(len(approved), approved[-1][1])
