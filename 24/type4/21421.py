#re
# from re import finditer
# with open(r'../files/24_21421.txt') as file:
#     data=file.readline()
#
# pattern=r'[1-9A-B][0-9A-B]*[02468A]'
# matches=[x.group() for x in finditer(pattern,data)]
# print(len(max(matches,key=len)))

#zamena
from string import printable
with open(r'../files/24_21421.txt') as file:
    data=file.readline()
# alph=printable[0:10:2]+'A'
# for i in alph:
#     data=data.replace(i,'!')
#
# for i in set(data):
#     if i!='!':
#         data=data.replace(i,' ')
# data=data.split()
# print(len(max(data,key=len))+1)
with open(r'../files/24_21421.txt') as file:
    data=file.readline().lower()
for i in printable[12:]:
    data=data.replace(i,' ')
data=data.split()
ans=0
for line in data:
    line=line.lstrip('0').rstrip('123579b')
    ans=max(ans,len(line))
print(ans)




