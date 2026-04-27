from fnmatch import fnmatch

for n in range(123222-123222%2024,10**10+1,2024):
    if fnmatch(str(n),'1*2322?2'):
        print(n,n//2024)