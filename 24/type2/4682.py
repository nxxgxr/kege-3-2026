#замена
# with open(r'../files/24_4682.txt') as file:
#     data=file.readline()
#
# for i in set(data):
#     if i in 'AE':
#         data=data.replace(i,'!')
#     else:
#         data=data.replace(i,'*')
# data=data.replace('!*','^')
# for i in set(data):
#     if i!='^':
#         data=data.replace(i,' ')
#
# data=data.split()
# print(len(max(data,key=len)))

#перебор

# with open(r'../files/24_4682.txt') as file:
#     data=file.readline()
# max_ans=0
# cnt=1
# for i in range(len(data)-1):
#     if data[i] in 'AE' and data[i+1] in 'BCD':
#         cnt=0
#         for x in range(i,len(data)-1,2):
#             if data[x] in 'AE' and data[x + 1] in 'BCD':
#                 cnt+=1
#             else:
#                 break
#     max_ans = max(max_ans, cnt)
# print(max_ans)


#re
with open(r'../files/24_4682.txt') as file:
    data=file.readline()