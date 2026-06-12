with open(r'../files/26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

mest = [m] * (k + 1)
for row, place in places:
    mest[place] = min(mest[place], row - 1)
ans = []
for i in range(1, k):
    ans += [[min(mest[i], mest[i + 1]), i]]

print(*max(ans, key=lambda x: (x[0], -x[1])))