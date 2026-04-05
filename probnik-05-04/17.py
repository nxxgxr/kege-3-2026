with open(r'./17 (1).txt') as file:
    data=[int(x) for x in file]
maxx=max(i for i in data if len(str(i))==2)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=len(str(num1))==2
    u2=len(str(num2))==2
    if u1+u2==1:
        u3= (num1+num2) % maxx ==0
        if u3:
            ans+=[num1+num2]
print(len(ans),max(ans))
