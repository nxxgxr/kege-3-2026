def convert(num,sys):
    res=''
    while num != 0:
        res += str(num%sys)
        num //= sys
    return res[::-1]

blin=[]
for x in range(1,2031):
    sum=convert(7 ** 170 + 7 ** 100 - x,7)
    kapec= sum.count('0')
    blin.append([kapec,x])
print(max(blin))





