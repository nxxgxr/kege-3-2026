#zamena
# from itertools import *
# with open(r'../files/24_7600.txt') as file:
#     data=file.readline()
# for val in product('QRS',repeat=2):
#     val=''.join(val)
#     data=data.replace(val,'1 1')
# data=data.split()
# print(len(max(data,key=len)))


#перебор
# with open(r'../files/24_7600.txt') as file:
#     data=file.readline()
#
# max_ans=0
# cnt=1
# for i in range(len(data)-1):
#     if data[i] in 'QRS' and data[i+1] in 'QRS':
#         max_ans=max(max_ans,cnt)
#         cnt=1
#     else:
#         cnt+=1
#     max_ans = max(max_ans, cnt)
# print(max_ans)

#re
with open(r'../files/24_7600.txt') as file:
    data=file.readline()





