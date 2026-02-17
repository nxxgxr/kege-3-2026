def convert(s,osn):
    stepen = len(s) - 1
    su = 0
    for j in s:
        su += alphabet.index(j) * osn ** stepen
        stepen -= 1
    return su
alphabet = '0123456789' + ''.join(sorted('QWERTYUIOPASDFGHJKLZXCVBNM'))



for x in range(3,18):
    num1 = convert('sladost',36)
    num2= int(f'gadost',10*x)
    num3 = int(f'hallowen',55-x)
    num4= int(f'166729861760449',10)
    if num1+num2 - num3 + num4==0:
        print(x)
