from fnmatch import *

for n in range(5233 - 5233%98591, 10**10,98591):
    if fnmatch(str(n),'5?2*3?3?'):
        print(n,n//98591)