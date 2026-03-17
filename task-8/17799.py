from itertools import *
rus='агемнрту'
alph=sorted('аргумент')
cnt=0
for val in product(alph,repeat=4):
    val=''.join(val)
    cnt+=1
    if rus.index(val[0]) < rus.index(val[1]) <rus.index(val[2]) < rus.index(val[3]) :
        chet=0
        for i in val:
            if val.count(i)>1:
                chet+=1
        if chet==0:
            print(cnt,val)