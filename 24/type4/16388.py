with open(r'../files/24_16388.txt') as file:
    data=file.readline()
from re import finditer
pattern=r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
q=[x.group() for x in finditer(pattern,data)]
print(len(max(q,key=len)))