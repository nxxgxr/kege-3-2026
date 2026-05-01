from re import finditer

with open(r'../files/24_1975.txt') as file:
    data = file.readline()

pattern=r'(?=P)P([^P]+P)+[^P]+P(?<=P)'

matches=[x.group() for x in finditer(pattern,data)]
print(len(max(matches,key=len)))

