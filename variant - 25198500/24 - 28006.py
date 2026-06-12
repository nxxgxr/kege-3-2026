from re import finditer

with open(r'files/24_28006.txt') as file:
    data=file.readline()

pattern=r'([(]([1-9][0-9]*[02468])[+-]([1-9][0-9]*[13579])[)])+'

q=[x.group() for x in finditer(pattern,data)]

print(len(max(q,key=len)))