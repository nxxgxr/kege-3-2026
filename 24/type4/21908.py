#re
from re import finditer

with open(r'../files/24_21908.txt') as file:
    data=file.readline()

pattern=r'[1-9A-D][0-9A-D]*[02468AC]'
q=[x.group() for x in finditer(pattern,data)]
print(len(max(q,key=len)))
print(len(max(q,key=lambda x: int(x,14) )))
# print(max(q,key=lambda x: int(x,14) ))



#zamena
from string import *
with open(r'../files/24_21908.txt') as file:
    data=file.readline().lower()
for i in printable[14:]:
    data=data.replace(i,' ')
data=data.split()
ans=0
for i in data:
    i=i.lstrip('0').rstrip('13579bd')
    ans=max(ans,len(i))
print(ans)
