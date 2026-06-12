# with open(r'../files/26_23208.txt') as file:
#     n = int(file.readline())
#     details = []
#     for num, line in enumerate(file, start=1):
#         grind, paint = map(int, line.split())
#         details += [[grind, 'G', num]]
#         details += [[paint, 'P', num]]
# details = sorted(details)
# conveyor = [0] * n
# last = []
# cnt = 0
# for detail in details:
#     if detail[2] not in conveyor:
#         if detail[1] == 'G':
#             conveyor[conveyor.index(0)] = detail[2]
#             cnt += 1
#         else:
#             conveyor[n - conveyor[::-1].index(0) - 1] = detail[2]
#         last = detail
# print(last[2], cnt - 1 if last[1] == 'G' else cnt)

#########################################


with open(r'../files/26_23208.txt') as file:
    n = int(file.readline())
    details = []
    for num, line in enumerate(file, start=1):
        grind, paint = map(int, line.split())
        if grind < paint:
            details.append([grind,'G',num])
        else:
            details.append([paint,'P',num])
details=sorted(details)
cnt_grind=sum(1 for x in details if x[1]=='G')
print(details[-1][2],cnt_grind -1 if details[-1][1]=='G' else cnt_grind)

