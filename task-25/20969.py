from fnmatch import fnmatch
for n in range(192368-192368%154682,10**11,154682):
    if fnmatch(str(n),'*192?3*68') and n % 154682==0:
        print(n,n//154682)
