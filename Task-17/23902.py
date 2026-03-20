with open(r'./files/17_23902.txt') as file:
    data=[int(x) for x in file]

ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=str(num1)[0] == str(num1)[-1]
    u2=str(num2)[0] == str(num2)[-1]
    u3=str(num3)[0] == str(num3)[-1]
    if u1+u2+u3 ==1:
        u4=len(str(num1))==4 and str(num1)[1]=='2'
        u5=len(str(num2))==4 and str(num2)[1]=='2'
        u6=len(str(num3))==4 and str(num3)[1]=='2'
        if u4+u5+u6 ==2:
            ans+=[max(num1,num2,num3)]

sm=sum(ans)
print(len(ans),sm)

