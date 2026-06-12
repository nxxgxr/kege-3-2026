with open(r'./files/9.txt') as file:
    data=[list(map(int,i.split())) for i in file]

for line in data:
    u1=line[0]<line[1]<line[2]<line[3]<line[4]<line[5]
    chet=[x for x in line if x%2==0]
    nechet=[x for x in line if x%2==1]
    u2=len(chet)==len(nechet)
    if u1+u2==2:
        print(sum(line))
