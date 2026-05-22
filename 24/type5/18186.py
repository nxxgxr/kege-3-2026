with open(r'../files/24_18186.txt') as file:
    data=file.readline()
dlina=ans=cnt=l=0
glas='AE'
soglas='BCDFGH'
flag=0
for r in range(len(data)-2):
    if data[r] in soglas and data[r+1] in soglas and data[r+2] in glas:
        if flag==0:
            l=r
            flag=1
        else:
            ans=max(ans,r-l+3)
            l=r
print(ans)
from re import finditer
G = r'[AE]'
S = r'[BCDFGH]'
pattern = rf'(?<={S}{S}{G}).+?(?={S + S + G})'
matches=[match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)) + 6)