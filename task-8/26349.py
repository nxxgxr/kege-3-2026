from itertools import *
alph=sorted('сулак')

for p in range(1,100):
    cnt=0
    for val in product(alph, repeat=p):
        cnt+=1
        val=''.join(val)
        glas=0
        if val[0] in 'лс' and ('аа' not in val and 'уа' not in val and 'ау' not in val and 'уу' not in val ):
            for i in val:
                if i in 'уа': glas+=1
            if glas<=2 and cnt==12368:
                print(p)

