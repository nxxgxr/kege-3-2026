with open(r'../files/26_17643.txt') as file:
    n = int(file.readline())
    tovar = []
    for line in file:
        ID, price, status = map(int, line.split())
        tovar += [[ID, price, status]]

tovar = sorted(tovar, key=lambda x: x[1])
mediana = sum(i[1] for i in tovar) / n

goods = {}
for ID, price, status in tovar:
    if price > mediana:
        if ID not in goods:
            goods[ID] = [not status, price, status]
        else:
            goods[ID][2] += status
            goods[ID][0] += (not status)

keys= sorted(goods, key=lambda x: (goods[x][0],goods[x][1],-goods[x][2]))
print(goods[keys[-1]][0] * goods[keys[-1]][1],goods[keys[-1]][-1])
