
with open(r'./files/26_4660.txt') as file:
    n=int(file.readline())
    product=[int(x) for x in file]
product=sorted(product)
skidka=n//4
odnim=sum(product) - sum(product[:skidka])/2
ans=[]
cnt=0
for i in product[::-1]:
    cnt +=1
    if cnt<4:
        ans+=[i]
    if cnt==4:
        ans+=[i/2]
        cnt=0


print(sum(ans),odnim)