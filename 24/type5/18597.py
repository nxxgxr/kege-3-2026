from re import finditer
with open(r'../files/24_18597.txt') as file:
    data=file.readline()
# num=r'([1-9][0-9]{3}[.]([0-9])+)'
# pattern=fr'{num}&{num}'
# matches=[match.group() for match in finditer(pattern,data)]
# print(len(max(matches,key=len)))

from string import printable
alph=printable[:10]
ans=cnt=dlina=l=0
flag=0
for r in range(len(data)-5):
    if data[r:r+4] in alph and data[r+4]=='.' and flag==0:
        l=r
        flag=1
    if data[r] == '.' and flag == 1:
        flag=1.5
    if data[r]=='.' and flag==1.5:
        cnt=dlina=0
        l=r
        flag=0
    if data[r]=='&':
        print(flag,l)
        if data[r+1:r+5] in alph and data[r+5]=='.':
            flag=2
        else:
            cnt = dlina = 0
            l = r
            flag = 0
    if flag==2 and data[r]=='.':
        dlina=r-l
        ans=max(ans,dlina)
        cnt = dlina = 0
        l = r
        flag = 0
print(ans)


data=data.split('&')
ans=0
for num1,num2 in zip(data,data[1:]):
    if '.' not in num1:
        continue
    dot1=num1.rfind('.')
    if dot1<4 or dot1==len(num1)-1 or '.' in num1[dot1-4:dot1]:
        continue
    num1=num1[dot1-4:]


    dot2=num2.find('.')
    if dot2==len(num2)-1 or num2[dot2 + 1]=='.' or dot2!=4:
        continue
    dot22 = num2.find('.',dot2+1)
    num2=num2[:dot22]
    ans=max(ans,len(num1+'&'+num2))
print(ans)
