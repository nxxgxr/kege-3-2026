with open(r'./files/26_5066.txt') as file:
    n=int(file.readline())
    kon=[int(x) for x in file]

kons=sorted(kon,reverse=True)
blocks=[]

while kons:
    block=[kons[0]]
    kons.remove(kons[0])
    for kon in kons[:]:
        if block[-1] - kon >=7:
            block+=[kon]
            kons.remove(kon)
    blocks+=[len(block)]
print(len(blocks),max(blocks))
