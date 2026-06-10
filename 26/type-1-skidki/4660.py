with open(r'../files/26_4660.txt') as file:
    n=int(file.readline())
    costs=[int(i)for i in file]
costs=sorted(costs)
price_2=sum(costs) - sum(costs[:n//4]) // 2
costs=sorted(costs,reverse=True)
price_1=sum(costs) -  sum(costs[3::4])//2
print(price_1,price_2)
