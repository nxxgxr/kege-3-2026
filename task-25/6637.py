from fnmatch import fnmatch
for n in range(121394-121394%3052,10**10,3052):
    if fnmatch(str(n),'1?2139*4') and n%3052==0:
        print(n,n//3052)