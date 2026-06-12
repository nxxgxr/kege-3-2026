
with open(r'../files/26_21910.txt') as file:
    b=int(file.readline())
    dlina=[int(x) for x in file]

dlina=sorted(dlina,reverse=True)

ans=[dlina[0]]
for i in dlina:
    if ans[-1] - i>=9:ans+=[i]
print(len(ans),ans[-1])



