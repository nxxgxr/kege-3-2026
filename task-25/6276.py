from fnmatch import fnmatch

for n in range(11111 - 11111%2023, 10**10 , 2023):
    if fnmatch(str(n), '1?1?1?1*1') and sum(map(int,str(n))) == 22:
        print(n)
