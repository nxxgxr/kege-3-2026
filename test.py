from string import printable
def f(num):
    res = ''
    while num != 0:
        print( num,num%39,printable[num%39])
        res += str(printable[num % 39])
        num //= 39
    return res[::-1]
print(f(12345678))
print(5*39**4 + printable.index('d')*39**3  + 4*39**2 + printable.index('v')*39 + printable.index('x'))