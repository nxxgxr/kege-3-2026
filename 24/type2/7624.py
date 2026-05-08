#замена
# from itertools import *
# with open(r'../files/24_7624.txt') as file:
#     data=file.readline()
#
# data=data.replace('X','!').replace('Y','!').replace('Z','!')
# data=data.replace('!!','1 1')
# data = data.split()
# print(len(max(data, key=len)))

# перебор
# with open(r'../files/24_7624.txt') as file:
#     data=file.readline()
#
# max_ans=0
# cnt=1
# for i in  range(len(data)-1):
#     if  data[i] in 'XYZ' and data[i+1] in 'XYZ':
#         max_ans=max(cnt,max_ans)
#         cnt=1
#     else:
#         cnt+=1
#     max_ans = max(cnt, max_ans)
# print(max_ans)

#re
with open(r'../files/24_7624.txt') as file:
    data=file.readline()