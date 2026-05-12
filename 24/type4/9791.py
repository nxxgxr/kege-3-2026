#re
# from re import finditer
#
# with open(r'../files/24_9791.txt') as file:
#     data=file.readline()
#
# pattern=r'([0-9]*[A-F]*)+'
# matches=[x.group() for x in finditer(pattern,data)]
# print(len(max(matches,key=len)))
from string import printable

#zamena
# from string import printable as alp
# with open(r'../files/24_9791.txt') as file:
#     data=file.readline().lower()
# for i in alp[16:]:
#     data=data.replace(i,' ')
# while ' 0' in data:
#     data.replace(' 0',' ')
# data=data.split()
# print(len(max(data,key=len)))
#
# with open(r'../files/24_9791.txt') as file:
#     data=file.readline().lower()
# for i in alp[16:]:
#     data=data.replace(i,' ')
# ans=0
# data=data.split()
# for line in data:
#     ans=max(ans,len(line.lstrip('0')))
# print(ans)


#перебор
from string import printable
with open(r'../files/24_9791.txt') as file:
    data=file.readline()
cnt=ans=dlina=0
alph=printable[:10] + printable[36:36+6]
for r in range(len(data)):
    if data[r] =='0' and cnt==0:continue
    if data[r] in alph:cnt+=1
    if data[r] not in alph:
        ans=max(ans,cnt)
        cnt=0
print(ans)