with open(r'../files/24_2942.txt') as file:
    data=file.readline()
data='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACABABABAB'
data=data.replace('AB','!').replace('AC','!')
for i in set(data):
    if i!='!':
        data=data.replace(i,' ')
data=data.split()
print(len(max(data)))