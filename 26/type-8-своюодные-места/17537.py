with open(r'../files/26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    ryad = [list(map(int, i.split())) for i in file]
mest = [m] * (k + 1)
for row, place in ryad:
    mest[place] = min(mest[place], row - 1)
ans = []
for i in range(1,len(mest) - 1):
    if mest[i+1] and mest[i]<=mest[i+1]:
        ans += [[mest[i], i + 1]]
print(max(ans))
