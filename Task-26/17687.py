with open(r'./files/26_17687.txt') as file:
    n=int(file.readline())
    data=[int(x) for x in file]
tovar=sorted(data,reverse=True)
razn=sum(tovar) - sum(tovar[:n//9])
odnim=sum(tovar) - sum(tovar[8::9])
print(razn,odnim)
