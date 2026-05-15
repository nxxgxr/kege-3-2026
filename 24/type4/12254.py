with open(r'../files/24_12254.txt') as file:
    data = file.readline()

# ans = cnt = flag = norm = 0
# for i in range(len(data)):
#     if data[i] == 'Q' and data[i + 1:i + 4] == 'RSQ' and norm == 0:
#         cnt = 1
#         flag = 1
#     elif data[i:i + 2] == 'SQ' and data[i + 2:i + 5] == 'RSQ' and norm == 0:
#         cnt = 2
#         flag = 2
#     elif data[i:i + 3] == 'RSQ' and flag == 1:
#         cnt += 1
#         flag = 2
#         norm = 1
#     elif data[i:i + 2] == 'SQ' and flag == 2:
#         ans = max(ans, cnt)
#         cnt += 1
#         flag = 3
#     elif data[i] == 'Q' and flag == 3:
#         ans = max(ans, cnt)
#         cnt += 1
#         flag = 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 0
#         flag = 0
#         norm = 0
#     ans = max(ans, cnt)
# print(max(ans, cnt))

from re import finditer

pattern = r'(?:Q|QS)?(?:RSQ)+(?:RS?|S)?'
q = [x.group() for x in finditer(pattern, data)]
print(len(max(q, key=len)))
