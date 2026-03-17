with open(r'./files/17_25356.txt') as file:
    data=[int(x) for x in file]
maxx=max(i for i in data if str(i)[-2:]=='30')
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=len(str(abs(num1)))!=4 and len(str(abs(num2)))!=4 and len(str(abs(num3)))!=4
    u2=num1+num2+num3 > maxx
    if u1+u2==2:
        ans+=[num1+num2+num3]

print(len(ans),max(ans))