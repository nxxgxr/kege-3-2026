with open(r'./files/26_12113.txt') as file:
    n=int(file.readline())
    boxes=[int(i) for i in file]
boxes=sorted(boxes,reverse=True)
first=max(i for i in boxes if i%2==1)#тут менять старт
korobki=[first]
for i in boxes:
    if korobki[-1] % 2 != i%2 and korobki[-1] - i >=7:
        korobki+=[i]
print(len(korobki),korobki[-1])


