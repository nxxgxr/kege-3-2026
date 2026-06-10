
with open(r'./files/17_23376.txt') as file:
    data=[int(x) for x in file]
maxx=max(x for x in data if len(str(abs(x)))==5 and str(x)[-2:]=='37')**2
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=len(str(abs(num1))) == 5
    u2=len(str(abs(num2))) == 5
    if u1+u2==1:
        u3 = (num1+num2)**2 > maxx
        if u3:
            ans+=[num1+num2]
print(len(ans),max(ans))