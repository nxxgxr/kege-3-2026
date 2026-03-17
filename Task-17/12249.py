with open(r'./files/17_12249.txt') as file:
    data=[int(x) for x in file]
maxx=max(i for i in data if len(str(i))==5 and str(i)[-1]=='3')
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=str(num1)[-1]=='3' or str(num2)[-1]=='3' or str(num3)[-1]=='3'
    u2=num1+num2+num3<=maxx
    if u1+u2 == 2:
        ans+=[num1+num2+num3]
print(len(ans),max(ans))