with open(r'./files/17_11236.txt') as file:
    data=[int(x) for x in file]
minn=min(i for i in data if len(str(abs(i)))==2)**2
maxx=max(i for i in data if len(str(abs(i)))==4 and str(i)[-1]=='1')
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=num1>minn
    u2=num2>minn
    u3=num3>minn
    if (u1+u2+u3)==2:
        u4=abs(num1*num2*num3)%maxx==0
        if u4:
            ans+=[abs(num1)+abs(num2)+abs(num3)]
print(len(ans),max(ans))