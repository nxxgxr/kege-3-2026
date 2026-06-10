with open(r'../files/26_7274.txt') as file:
    n = int(file.readline())
    dlin = [list(map(int, i.split())) for i in file]

dlin = sorted(dlin)

for num1, num2 in zip(dlin, dlin[1:]):
    if num1[0] == num2[0]:
        if num2[1] - num1[1] == 14:
            print(num1[0], num1[1] + 1)
