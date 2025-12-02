blin=15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809

def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

r=convert(blin,7)
chet=0
nechet=0
for x in r:
    if int(x)%2 == 0:
        chet+=1
    else:
        nechet+=1
print(abs(chet-nechet))

