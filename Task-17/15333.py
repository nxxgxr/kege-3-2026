with open(r'./files/17_15333.txt') as file:
    data=[int(x) for x in file]
maxx=max(x for x in data if x%19==0)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=(num1>maxx) or (num2>maxx)
    if u1:
        ans+=[num1+num2]

print(len(ans),max(ans))