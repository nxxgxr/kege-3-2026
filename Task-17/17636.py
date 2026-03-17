with open(r'./files/17_17636.txt') as file:
    n=file.readline()
    data=[int(x) for x in file]
maxx=max(x for x in data if str(abs(x))[-1]=='3' and len(str(abs(x)))==3)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1=[1 for x in (num1,num2,num3) if str(abs(x))[-1]=='3' and len(str(abs(x)))==3]
    if len(u1)>=1:
        u2=num1+num2+num3 < maxx
        if u2:
            ans+=[num1+num2+num3]

print(len(ans),max(ans))