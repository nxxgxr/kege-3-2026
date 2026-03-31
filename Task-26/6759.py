with open(r'./files/26_6759.txt') as file:
    n=int(file.readline())
    data=[int(x) for x in file]
kolvo=n//3
data=sorted(data)
ans1=sum(data) - sum(data[-kolvo:])
ans2=sum(data) - sum(data[::-1][2::3])
print(ans1,ans2)