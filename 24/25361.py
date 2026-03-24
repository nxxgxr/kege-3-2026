with open('24_25361.txt') as file:
    data = file.readline()
ans=0
len=0
max_len=0
last=False
for i in data:
    if i in 'NOP':
        if last:
            len=1
        else:
            len+=1
        last = True
    else:
        len+=1
        last = False
    if len > max_len:
        max_len=len
print(max_len)
