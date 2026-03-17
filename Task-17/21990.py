with open(r'./files/17_21990.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
maxx=str(max(data))[-1]
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    otr=0
    pol=0
    if num1>=0:
        pol+=num1
    else:
        otr+=num1

    if num2>=0:pol+=num2
    else:otr+=num2

    if num3>=0:pol+=num3
    else:otr+=num3

    u1= abs(otr) <= pol
    u2=str(num1*num2*num3)[-1] == maxx
    if u1+u2==2:
        ans+=[abs(num1*num2*num3)]
print(len(ans),max(ans))

