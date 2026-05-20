from re import finditer
from sys import setrecursionlimit
setrecursionlimit(54737)
with open(r'../files/24_18239.txt') as file:
    data = file.readline()
num = r'[1-9]+'
pattern = rf'({num}[-])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
ans = 0

for match in matches:
    len_match = len(match)
    if eval(match) > -20_000:
        ans = max(len_match, ans)
    elif len_match > ans:
        for l in range(len_match):
            if match[l] == '-': continue
            for r in range(len_match - 1, l, -1):
                if match[r] == '-': continue
                new_match = match[l:r + 1]
                if eval(new_match) > -20_000:
                    ans = max(len(new_match), ans)
                    break
print(ans)
