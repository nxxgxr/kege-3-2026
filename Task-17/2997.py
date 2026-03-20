with open(r'./files/17_2997.txt') as file:
    data=[int(x) for x in file]
cifri=[int(str(abs(x))[1]) for x in data if len(str(abs(x)))==3]
maxx=max((cifri.count(i),i) for i in range(10))[1]
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=str(num1)[-1]==str(maxx)
    u2=str(num2)[-1]==str(maxx)
    if (u1+u2)>=1:
        ans+=[num1+num2]
print(len(ans),max(ans))

