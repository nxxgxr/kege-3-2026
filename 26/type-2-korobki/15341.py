
with open(r'../files/26_15341.txt') as file:
    n=int(file.readline())
    diam=[int(x) for x in file]
diam=sorted(diam,reverse=True)
cnt=1
last=diam[0]
for i in diam:
    if last-i>=8:
        cnt+=1
        last=i

print(cnt,last)
