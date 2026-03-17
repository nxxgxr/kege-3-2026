with open(r'./files/26_5988.txt') as file:
    n = int(file.readline())
    boxes = [[int(x.split()[0]), x.split()[1]] for x in file]
boxes=sorted(boxes,reverse=True)
dp = [1] * n
for i in range(n):
    for j in range(i):
        if boxes[j][0] >= boxes[i][0] + 7 and boxes[j][1] != boxes[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
max_len = max(dp)
min_size = min(boxes[i][0] for i in range(n) if dp[i] == max_len)
print(max_len, min_size)