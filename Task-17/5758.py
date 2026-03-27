with open(r'./files/17_5758.txt') as file:
    data=[int(x) for x in file]


for i in range(len(data)-1):
    for n in range(i+1,len(data)):
        num1=data[i]
        num2=data[n]

