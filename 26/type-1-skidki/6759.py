
with open(r'../files/26_6759.txt') as file:
    n=int(file.readline())
    cen=[int(x) for x in file]
cen=sorted(cen)
price_1=sum(cen) - sum(cen[::-1][:n//3])
# price_1=sum(cen[::-1][n//3:])
price_2=sum(cen) - sum(cen[::-1][2::3])
print(price_1,price_2)