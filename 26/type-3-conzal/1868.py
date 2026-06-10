with open(r'../files/26_1868.txt') as file:
    N = int(file.readline())
    ryad = [list(map(int, i.split())) for i in file]
ryad = sorted(ryad)[1:]
con = [ryad[0]]
ans = []
for x in ryad[1:]:
    if x[0] == con[-1][0]:
        if x[1] - con[-1][1] == 3:
            ans += [[x[0], con[-1][1] + 1]]
    con += [x]
print(ans[-1])
