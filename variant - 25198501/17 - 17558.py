with open(r'./files/17_17558.txt') as file:
    data=[int(x) for x in file]
summ=sum(1 for x in data if abs(x)%32 == 0)
ans=[]
for num1,num2 in zip(data,data[1:]):
    x= num1<0
    y= num2<0
    u1= x + y >=1
    u2= num1 + num2 < summ
    if u1+u2==2:
        ans+=[num1+num2]
print(len(ans),max(ans))