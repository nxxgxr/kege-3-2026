with open(r'./files/24_8510.txt') as file:
    data = file.readline()

max_len = 0
current_len = 0
last = False
for i in data:
    if i in 'NOP':
        if last:
            current_len = 1
        else:
            current_len += 1
        last = True
    else:
        current_len += 1
        last = False
    if current_len > max_len:
        max_len = current_len
print(max_len)