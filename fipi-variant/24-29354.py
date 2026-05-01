with open(r'./24_29354.txt') as file:
    data = file.readline()
max_len = 0
kolvo = 0
left = 0
for right in range(1, len(data)):
    if data[right] == 'C' and data[right - 1] == 'B':
        kolvo += 1
    if kolvo == 190:
        dlina = right - left + 1
        if dlina > max_len:
            max_len = dlina
    while kolvo > 190:
        if data[left] == 'B' and data[left + 1] == 'C':
            kolvo -= 1
        left += 1
print(max_len)
