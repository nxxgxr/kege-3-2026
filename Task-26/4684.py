with open(r'./files/26_4684.txt') as file:
    n=int(file.readline())
    product = [int(x) for x in file]
product = sorted(product)
skidka = n // 6
odnim = sum(product) - sum(product[:skidka]) / 2
ans=[]
cnt=0
for i in product[::-1]:
    cnt+=1
    if cnt<6:
        ans+=[i]

    if cnt==6:
        cnt=0
        ans+=[i/2]



print(sum(ans),odnim)