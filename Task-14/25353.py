from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res[::-1]


for x in range(1,27001):
    r=convert(3*27**9 + 2*27**6 + 27**3 - x,27)
    if r.count('0') == 6:
        print(x)
        break

