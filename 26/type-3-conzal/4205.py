with open(r'../files/26_4205.txt') as file:
    n=int(file.readline())
    mest=[list(map(int,i.split())) for i in file]
mest=sorted(mest)
for num1,num2 in zip(mest,mest[1:]):
    if num1[0] == num2[0]:
        if num2[1]-num1[1]==14:
            print(num1[0],num1[1]+1)




