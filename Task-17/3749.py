with open(r'./files/17_3749.txt') as file:
    data=[int(x) for x in file]

maxx=max(int(x) for x in data if x**.5 % 1 ==0) * 3
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1=(num1*num2)**.5 %1 ==0
    u2=num1 <= maxx
    u3=num2 <= maxx
    if u2+u3 >=1 and u1:
        ans+=[(num1*num2)**.5]
print(len(ans), min(ans)+max(ans))
