with open(r'./files/17_9786.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
maxx=max(x for x in data if str(x)[-2:]=='25')
ans=[]

for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=[1 for x in (num1,num2,num3) if len(str(abs(x)))==4]
    if len(u1)<=2 :
        u4=num1+num2+num3 <= maxx
        if u4:
            ans+=[num1+num2+num3]

print(len(ans),max(ans))