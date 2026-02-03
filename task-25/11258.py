from fnmatch import fnmatch
for n in range(75122-75122%8387,10**9,8387):
    if fnmatch(str(n),'*75?122*'):
        print(n,n//8387)