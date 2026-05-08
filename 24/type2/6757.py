#замена
# with open(r'../files/24_6757.txt') as file:
#     data=file.readline()
#
# data=data.replace('CFE','!').replace('FCE','!')
# for i in set(data):
#     if i!='!':
#         data=data.replace(i,' ')
# data=data.split()
# print(len(max(data,key=len)))


#перебор
# with open(r'../files/24_6757.txt') as file:
#     data=file.readline()
# cnt=0
# max_ans=0
# for i in range(len(data)-2):
#     if data[i:i+3] in 'CFE FCE':
#         cnt=0
#         for x in range(i,len(data)-1,3):
#             if data[x:x + 3] in 'CFE FCE':
#                 cnt+=1
#             else:
#                 break
#     max_ans=max(cnt,max_ans)
# print(max_ans)


#re
with open(r'../files/24_6757.txt') as file:
    data=file.readline()