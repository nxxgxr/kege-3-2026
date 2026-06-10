with open(r'../files/26_6641.txt') as file:
    n, m = map(int, file.readline().split())
    tovar = [list(map(int, i.replace('W', '1').replace('S', '0').split())) for i in file]
costs = sorted(tovar)
cnt_S = 0
bought = []
summ = 0
for cost in costs:
    if summ + cost[0] <= m:
        summ += cost[0]
        bought += [cost]
        cnt_S += 1 if cost[1] == 0 else 0
len_bought = len(bought)
for cost_1 in bought[::-1]:
    if cost_1[1] == 1:
        for cost_2 in costs[len_bought:]:
            len_bought += 1
            if cost_2[1] == 0:
                if summ - cost_1[0] + cost_2[0] <= m:
                    bought.remove(cost_1)
                    bought += [cost_2]
                    cnt_S += 1
                    summ += cost_2[0] - cost_1[0]
                    break
print(cnt_S, m - summ)
