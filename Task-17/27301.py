with open(r'./files/17_27301.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
maxx=max(x for x in data if str(abs(x))[:2]=='45')
ans=[]
ans2=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    otr=0
    if num1<0:otr+=1
    if num2<0:otr+=1
    if num3<0:otr+=1
    u1=otr==1
    u2= num1+num2+num3 >=maxx
    if u1+u2==2:
        ans+=[num1+num2+num3]
        if str(num1+num2+num3)[-2:]=='45':
            ans2+=[num1+num2+num3]





print(len(ans),min(ans2))

