def convert(num,sys):
    res=''
    while num:
        res+=str(num%sys)
        num//=sys
    return res[::-1] if res else '0'

ans=[]
ar = 0
an = 0

for n in range(1,100000):
    s=convert(n,5)
    if s[-1] == '0':
        s=s.replace('1','*')
        s=s.replace('4','1')
        s=s.replace('*','4')
        r_str='33'+s
    else:
        r_str='3'+s[1:]+'42'
    r=int(r_str,5)
    if r<1922:
        if r>ar:
            ar=r
            an=n
print(an)