with open(r'../files/26_23383.txt') as file:
    n = int(file.readline())
    sportsmen = [list(map(int, i.split())) for i in file]
sportsmen = sorted(sportsmen, key=lambda x: (x[1], x[0]))
ans = 0
cnt = 1
point = 0
for i in range(len(sportsmen) - 1):
    if sportsmen[i][1] == sportsmen[i + 1][1] and sportsmen[i][0] + 1 == sportsmen[i + 1][0]:
        cnt += 1
    elif sportsmen[i][0] == sportsmen[i + 1][0]:
        continue
    else:
        ans = max(ans, cnt)
        cnt = 1
    if cnt > ans:
        ans = cnt
        point = sportsmen[i][1]
print(ans, point)
