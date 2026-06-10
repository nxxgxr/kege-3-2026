with open(r'../files/26_4604.txt') as file:
    N = int(file.readline())
    dlina = [int(x) for x in file]
dlina = sorted(dlina, reverse=True)
ans1 = [dlina[0]]
for i in dlina:
    if ans1[-1] - i >= 3:
        ans1 += [i]
print(len(ans1), ans1[-1])
