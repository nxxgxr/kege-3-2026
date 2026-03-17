with open(r'./files/17_9748.txt') as file:
    data=[int(x) for x in file]
mx=max(i for i in data if str(i)[-2:]=='15')
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=num1+num2+num3>=mx
    u2=len(str(num1))==4
    u3=len(str(num2))==4
    u4=len(str(num3))==4
    if u2+u3+u4 ==1 and u1:
        ans+=[num1+num2+num3]
print(len(ans),max(ans))

