with open(r'./files/26_4629.txt') as file:
    n=file.readline()
    product=[int(x) for x in file]
product=sorted(product)
kolvo=int(n)//4
vsego=sum(product)
pokyp=sum(product[-kolvo:])//2
magaz=sum(product[:kolvo])//2
print(vsego-pokyp,vsego-magaz)


