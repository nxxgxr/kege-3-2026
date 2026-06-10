with open(r'../files/26_4629.txt') as file:
    N = int(file.readline())
    costs = [int(x) for x in file]
costs = sorted(costs, reverse=True)
price_1 = sum(costs) - sum(costs[3::4]) // 2
price_2 = sum(costs) - sum(costs[3 * N // 4:]) // 2
print(price_1, price_2)
