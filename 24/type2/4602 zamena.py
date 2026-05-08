with open(r'../files/24_4602.txt') as file:
    data=file.readline()

for i in set(data):
    if i in 'BCD':
        data=data.replace(i,'*')
    else:
        data=data.replace(i,'!')

data=data.replace('*!','^')
for i in set(data):
    if i!='^':
        data=data.replace(i,' ')
data=data.split()
print(len(max(data,key=len)))