with open(r'./files/7030.txt') as file:
    data=[list(map(int,i.split())) for i in file]
def treyg(x,y,z):
    if (x**2 == y**2 + z**2) or (y**2 == z**2 + x**2) or (z**2 == x**2 + y**2):
        return True
    return False
cnt=0
for line in data:
    amount=[line.count(i) for i in set(line)]
    if sorted(amount)==[2,2,2]:
        if treyg(list(set(line))[0],list(set(line))[1],list(set(line))[2]):
            cnt+=1

print(cnt)