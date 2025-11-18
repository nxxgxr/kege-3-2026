def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for n in range(1,1000000):
    r=convert(n,3)
    b = sum(map(int, r))
    if b%2==0:
        r= '12' +r[2:]+'0'
    else:
        r='10' + r[2:] + '2'
    r=int(r,3)
    if r>105:
        print(n,r)
        break